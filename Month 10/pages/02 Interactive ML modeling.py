"""
A dashboard for interactively querying a pre-trained ML model.
This can be a useful way to explore or demo a model.
"""
import time

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from sklearn import metrics
from sklearn.datasets import make_circles, make_classification, make_moons
from sklearn.ensemble import AdaBoostClassifier, HistGradientBoostingClassifier
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import ComplementNB, GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MaxAbsScaler
from sklearn.tree import DecisionTreeClassifier

# st.set_page_config(layout="wide")


def generate_data():
    """Generate all the datasets to be loaded for explortion.
    Add more datasets here--the main body of the code below loops
    over the returned dictionary and automatically populates `st.expander()`
    sections with the results."""
    datasets = {}
    # linearly separable data
    X, y = make_classification(
        n_samples=10_000,
        n_features=2,
        n_redundant=0,
        n_informative=2,
        random_state=1,
        n_clusters_per_class=1,
    )
    rng = np.random.RandomState(2)
    X += 2 * rng.uniform(size=X.shape)
    datasets["Linearly Separable"] = train_test_split(X, y, train_size=0.8, random_state=0)

    # circles dataset
    x, y = make_circles(n_samples=(9000, 1000), noise=0.2, factor=0.5, random_state=0)
    datasets["Circles"] = train_test_split(x, y, train_size=0.8, random_state=0)

    # moons dataset
    x, y = make_moons(n_samples=(4000, 1000), noise=0.4, random_state=0)
    datasets["Moons"] = train_test_split(x, y, train_size=0.8, random_state=0)

    return datasets


def plot_cutoff_results(y_true, pred, cutoff):
    """Plot the data, showing the true values, plus the predictions and decision
    boundaries for `clf`."""
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.kdeplot(x=pred, hue=y_true, ax=ax, common_norm=False)
    ax.axvline(cutoff, color="red", linestyle="--")
    ax.set_title("Distribution of predictions, with cutoff value")
    return fig


def accuracies(true, preds, cutoff=0.5):
    """Return a DataFrame for the confusion matrix, based on the cutoff
    provided for the predictions."""
    accuracies = pd.DataFrame(
        [
            {"Metric": "Accuracy", "Score": metrics.accuracy_score(test_y, preds >= cutoff)},
            {"Metric": "F1", "Score": metrics.f1_score(test_y, preds >= cutoff)},
            {"Metric": "AUC-ROC", "Score": metrics.roc_auc_score(test_y, preds)},
            {"Metric": "Log Loss", "Score": metrics.log_loss(test_y, preds)},
            {"Metric": "Brier Score", "Score": metrics.brier_score_loss(test_y, preds)},
        ]
    )

    # Manually generate a confusion matrix with better column/index names.
    true_pos = sum((preds == 1) & (true == 1))
    true_neg = sum((preds == 0) & (true == 0))
    false_pos = sum((preds == 0) & (true == 1))
    false_neg = sum((preds == 1) & (true == 0))
    cm = pd.DataFrame(
        [[true_pos, false_neg], [false_pos, true_neg]],
        columns=pd.MultiIndex.from_tuples(
            [
                ("Predicted", "Positive"),
                ("Predicted", "Negative"),
            ]
        ),
        index=pd.MultiIndex.from_tuples(
            [
                ("Actual", "Positive"),
                ("Actual", "Negative"),
            ]
        ),
    )
    return accuracies, cm


# WHen caching any matplotlib figures, Streamlit will normally hang.
# This little fix (borrowed from someone on the Strealit forums)
# specifies a custom hash function for Matplotlib figures
# which seems to work.
@st.cache(hash_funcs={mpl.figure.Figure: lambda _: None})
def generate_model_result(clf, train_x, test_x, train_y, test_y):
    """Fit the model, and generate all the stuff that we need to output
    for the dashboard."""
    # Fit the model and generate test set predictions
    model = Pipeline([("scaler", MaxAbsScaler()), ("clf", clf)])
    fit_time = time.time()
    model.fit(train_x, train_y)
    fit_time = time.time() - fit_time

    # test set predictions
    preds = model.predict_proba(test_x)[:, 1]

    # Plot of the data + decision boundaries
    x = np.vstack((train_x, test_x))
    y = np.concatenate((train_y, test_y))
    fig1, ax = plt.subplots(figsize=(10, 5), ncols=2, sharex=True, sharey=True)
    ax[0].scatter(x[:, 0], x[:, 1], c=y, cmap="bwr", s=1)
    DecisionBoundaryDisplay.from_estimator(
        model,
        x,
        grid_resolution=100,
        ax=ax[1],
        alpha=0.25,
        cmap="bwr",
    )
    ax[0].set_title("Original Data")
    ax[1].set_title("Decision Boundary")

    return fit_time, fig1, preds, test_y


if __name__ == "__main__":
    datasets = generate_data()

    # Let the user select the model to fit.
    models = {
        "Decision Tree": DecisionTreeClassifier(random_state=0),
        "Logistic Regression": LogisticRegression(random_state=0),
        "Multi Layer Perceptron": MLPClassifier(
            (256, 256, 256, 256),
            random_state=0, max_iter=2000),
        "Gaussian Naive Bayes": GaussianNB(),
        "Complement Naive Bayes": ComplementNB(),
        "Adaboost": AdaBoostClassifier(random_state=0),
        "Histogram Gradient Boosting": HistGradientBoostingClassifier(random_state=0),
    }

    st.title("Comparison of different scikit-learn models")
    st.markdown(
        """
        This dashboard allows you to inspect the different predictions from
        a few different models on a simple binary classification task.  This
        is basically a re-creation of scikit-learn's [Classifier Comparison](https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html)
        page, but in Streamlit, and with more interactivity.
          
          
        Here's the overview of what this app does:
        
        1. Loads the data and generates a balanced train-test split.
        1. Fits a few different models to that data.  No parameter tuning is done
            in this demo just for the sake of time.
        1. Allows the user to select a model to investigate, and displays some
            important information about that model's fit statistics:
            1. Time to fit, plus a few accuracy statistics.
            1. A visualization of the data, and the decision boundary learned by the model.
        1. Allows the user to input an X-Y point, and have the prediction for that point
            be shown.
        
        There is a lot of caching used in this particular app, so it may run a bit
        slow the first time you open it or fit a model, but it should save the results
        and be very quick to re-run!
        """
    )

    model_selector = st.selectbox(
        "Select a model to fit and investigate.",
        models.keys(),
    )
    model = models[model_selector]
    for dataset in datasets.keys():
        with st.expander(dataset):
            # fit_time, data, preds, test_y = generate_model_result(model, *generate_data())
            fit_time, data, preds, test_y = generate_model_result(model, *datasets[dataset])
            st.pyplot(data)
            cutoff_plot = st.empty()

            st.write(f"Fit time: {fit_time:.3f}s")
            cutoff_value = st.slider(
                "Select a cutoff value for converting soft-margin predictions to hard-margin.",
                min_value=float(np.min(preds)),
                max_value=float(np.max(preds)),
                value=0.5,
                # Sometimes you need to pass a unique `key` kwarg to input widgets,
                # usually if you're creating multiple of them in a loop--like we are now.
                # The unique `key` value lets Streamlit track what data comes from where.
                key=dataset,
            )
            cutoff_plot.pyplot(plot_cutoff_results(test_y, preds, cutoff_value))
            acc, cm = accuracies(test_y, preds, cutoff_value)
            c1, c2 = st.columns(2)
            with c1:
                st.write("Accuracy Metrics")
                st.table(acc)
            with c2:
                st.write("Confusion Matrix")
                st.table(cm)