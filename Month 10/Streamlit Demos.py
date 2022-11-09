import streamlit as st

if __name__ == "__main__":
    st.title("Streamlit Dashboards!")
    st.markdown(
        """
        Today we're covering Streamlit dashboards.  Unlike other sessions,
        I'll be working from PyCharm and my web browser.
        
        Instructions for how to run these files will be in the README.md file
        when this is all uploaded to GitHub.
        
        (This might be a session that doesn't run the full 2 hours, we'll see!)
        
        # Streamlit Dashboards are web applications
        
        Streamlit will run a local web server on your machine.  It will be accessible
        to other machines _on your network_ unless you change a configuration setting.
        But, this only sets up _Streamlit_ to _listen_ for connections from the network;
        if you have firewall rules or other network-level security settings in place,
        this won't override them.  (E.g.: a computer set to drop all incoming connections,
        running Streamlit dashboards, will not have those dashboards accessible over the
        network).
        
        You can use this, though, to easily deploy your Streamlit dashboards either publicly
        (e.g. on an AWS server or something that's public facing) or just on your network,
        e.g. your university's network, or your research group's sub-network, or wherever.
        
        # Streamlit is meant to be quick to build in
        
        Streamlit can produce some very pretty and elaborate dashboards, but I find its
        real strength is in _quicky_ putting a frontend on something.  It makes it very
        easy (as we'll see) to go from zero to a pretty solid, working dashboard.
        
        However, there is a lot that it doesn't do, or doesn't do super well.  Other dashboarding
        libraries might offer more depth (Dash, which is made by the Plotly team, seems like
        one such alternative), and there's always the option of using a web development framework
        like Flask or Django to write something yourself.  But, that's going to require
        a lot more time and extra expertise.
        
        Streamlit dashbaords also work best when they're _primarily static_ and have _limited
        interactivity._  They do support interactivity, but it's not as pervasive as some other
        dashboard tools (especially all-in-one, dedicated products).  Streamlit doesn't really
        support paradigms like "double-click the graph to drill down" or "drag and drop to
        customize your own interface."
        
        ...but then, you rarely _need_ that level of interaction, most of the time.  A well-designed
        dashboard can be made with minimal, or basic, interactions, and still do everything it
        needs to do.
        
        # Install streamlit
        
        Installing Streamlit is easy:
        
        ```bash
        conda install streamlit
        ```
        
        There are also a lot of streamlit "plugins" from various libaries--like spaCy--
        that add additional functionality to Streamlit dashboards.
        
        # Other dashboard options
        
        There are a lot of other dashboard tools out there in Python!
        
        - Dash, from Plotly.
            - Dash, from my brief experience, feels a lot like Javascript development.
              A lot of direct interfacing with HTML elements, linking elements together
              in dependency graphs, things like that.  Dash even described itself as 
              "React for Python" when it was first launched (React as in React.js, one
              of the biggest Javascript frameworks for web development).
        - Panel, from Anaconda
        - Voila, from QuantStack.
            - Voila seems geared at turning Jupyter notebooks into dashboards.  So if
              you use a lot of Jupyter notebooks, maybe give this one a look.
        
        I haven't used these, but they seem to offer a lot more control than Streamlit--
        at the expense of being more complicated to use.  Streamlit, by contrast, tries
        to minimize the amount of work it takes to put a dashboard frontend on your
        _already existing code._  And from my experience, it does a _really_ good
        job.
        
        Of course, there are a few not-strictly-dashboard tools that can still work like
        dashboards:
        
        - Jupyter notebooks can render interactive components like sliders.  This can
            be useful for deploying interactive code, e.g. for CS education or data
            analysis education, but it's not quite a dashboard in the usual sense.
        - Bokeh--the Python plotting libary that's all about maximum and pervasive
            interactivity--can kind of be used as a dashboard library.  It might take
            a lot of work, though, using just plain Bokeh.  But you can always embed
            a Bokeh plot in Streamlit (using `st.bokeh()`) to get the best of both worlds!
        - You can, of course, always roll your own dashboard fully from scratch using
            any of Python's web development frameworks like Flask or Django.  This offers
            maximum control, but of coure, requires the most work. 
        """
    )
