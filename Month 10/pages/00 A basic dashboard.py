"""
Run this file not with `python [file].py`, but with `streamlit run [file.py]`
"""
import time

import streamlit as st

# Set some general page-wide configuration options, like the page title
# tht appears in the browser/tab name, and whether to use the "wide"
# layout--which uses as much horizontal space as possible--or the "centered"
# layout--which uses a narrower column in the center of the screen.
st.set_page_config(
    page_title="Basic Dashboard",
    # layout="wide",
)

if __name__ == "__main__":
    st.title("A rapid-fire tour of Streamlit: the absolute basics")
    st.markdown(
        """
    This is a dashboard showing off the very basics.  It's a bit messy, since the
    aim is to demonstrate different major elements of Streamlit dashboards.

    You can write text using basic Markdown formatting using `st.markdown()`.
    - Bulleted lists!
    - More bullets!

    1. Numbered lists!
    1. More numbers!

    _Italics!_  **Bold!** **_Bold Italics!_**

    And more.  Check out the [Markdown cheat sheet](https://www.markdownguide.org/cheat-sheet/).  (Streamlit might not
    support eveything there, but it should support all the basic stuff).
    """
    )

    st.markdown("You can also use `st.latex()` to embed LaTeX math equations.")
    st.latex(r"""
    e = \sum^{\infty}_{1} \frac{1}{n!} = \frac{1}{1} + \frac{1}{1\times 2} + \frac{1}{1\times 2\times 3} + \cdots
    """)

    st.markdown("You can include images with st.image():")
    st.image("images/Spot_the_Cow.png")

    # st.text_input() and st.text_area(): get text input from the user.
    # They return whatever text the user input, as a string.
    text = st.text_input("Put some text here to generate a title below.:")
    if text != "":
        st.write(f"Your text is: {repr(text)}")
        st.markdown(
            f"""
        # {text}

        {text.upper()}!!!"""
        )

    st.markdown(
        """
    You can also use `streamlit.write()` to pretty-print almost any Python object.
    """
    )
    my_dict = {
        "Henry": {
            "Cats": ["Hermes", "Casper"],
        },
        "George": {
            "Cats": 0,
        },
    }
    st.write(my_dict)

    st.markdown(
        """
    # Other interactivity

    There are a few different options for numeric inputs:
    """
    )
    slider = st.slider("I'm a slider!", min_value=0, max_value=100, step=17)
    st.write(f"The value of the slider is: {slider}")
    st.markdown(
        """
    Note that the text doesn't update until the slider stops moving.  This is how
    Streamlit is intended to work: nothing updates until a value is finalized, e.g.,
    until the slider has been released.
    """
    )

    number = st.number_input("Type a number:", value=10)
    st.write(f"The square of the number you chose is: {number**2}")

    st.markdown(
        """
    # Sections and organization

    You can have collapsible sections with `st.expander()`:
    """
    )
    with st.expander("Click me!"):
        st.write("Lorem ipsum dolor sit amet and all that.")
        st.slider("You can embed anything in an expander.")

    st.markdown("You can also do multi-column arrangements:")
    col1, col2 = st.columns(2)
    with col1:
        st.write("I'm the first column!")
        st.slider("I'm a slider in a column!")

    with col2:
        st.write("I'm the second column!")

    st.markdown(
        """
    # `st.empty()` for manually updating in-place

    In Streamlit, objects are rendered to the screen as soon as the
    function is called, and are rendered at the very bottom of the page.
    If you need to make a "placeholder," use `st.empty()`.

    First, let's see how this can go wrong.  When the buton below is clicked,
    we want the dashboard to update a text box to show an incremented counter.
    But instead, it will draw a bunch more text boxes.
    """
    )
    with st.expander("The wrong way to update text boxes"):
        if st.button("Click here to start updating the wrong way."):
            for i in range(100):
                st.text(i)
                time.sleep(0.1)

    st.markdown("""
    What happened is that in the for loop, every time streamlit saw `st.text()`,
    it _added a new text element._  To make this behave the way we want it to,
    we need to create a single Streamlit element, then update _only that one element._

    To do this, we have `st.empty()`.  This creates, basically, a general-purpose
    container in our dashboard.  Basically everything that exists as a Streamlit
    function can be called on this as a method.  Doing so will clear out the contents
    of this container and re-render the contents based on whatever method we call.

    So instead of calling `st.write()`, we would do:

    ```python
    placeholder = st.empty()
    placeholder.write(...)
    ```

    Let's see this in action.
    """)
    live_updates = st.empty()
    if st.button("Click here to start updating the right way."):
        for i in range(100):
            live_updates.write(i)
            time.sleep(0.1)

    """
    # Streamlit Magic

    If you have a comment, either with a `#` or with triple-quotes,
    Streamlit will, by default print that out.  This text will automatically
    populate in the dashboard as if written with `st.markdown()`.

    (This behavior can be disabled).
    """