"""
A bit about Streamlit configuration.
"""

import streamlit as st

if __name__ == "__main__":
    st.markdown(
        """
    # Streamlit Configuration
    
    Some of Streamlit's options can be configured through a configuration file, or
    through environment variables.  The configuration file approach is probably
    better.
    
    There are two places you can put this config file.  Either you can use a
    _global_ config file, or you can use a _per-project_ config file.
    
    - Global config file is located at `~/.streamlit/config.toml` for Mac/Linux,
      and `%userprofile%/.streamlit/config.toml`
    - Per-project config file is located at `.streamlit/config.toml`, inside the
      project directory.
      
    Some of the option you may wish to change:
    ```toml
    [brower]
    gatherUsageStatistics = true
    ```
    
    This setting (`true` by default) will collect anonymous usage statistics to 
    send back to the Streamlit developers.  They do not see any of the data or
    code you've written.  Set this to `false` (all lowercase!) to disable this
    behavior.
    
    ```toml
    [browser]
    serverAddress = "localhost"
    ```
    
    This determines where Streamlit opens the web server.  By default, `"locahlost"`
    allows you and anyone on your network to access the dashboard if they know
    the IP address of your computer (but: any firewall rules you have configured
    can block any incoming traffic and prevent people from accessing the dashboard).
    I recommend changing this to `"127.0.0.1"`, which is like `"localhost"`, but it
    does not open the dashboard up to any other computers on the network.
    
    ```toml
    [runner]
    enableMagic = true
    ```
    
    Enables Streamlit's "magic" formatting: any text, comments, or function return values
    not explicitly stored in a variable will be written to the page using `st.write()`.
    Set this to `false` to change this behavior, and only display content you explicitly
    create with one of the Streamlit functions.
    
    ```toml
    [server]
    maxUploadSize = 200
    ```
    
    If you're using a file upload widget, the maximum file size is 200mb by default.
    Change this to a larger number if you need to upload larger files.
    
    ```toml
    [theme]
    base = "dark"
    # primaryColor = 
    # backgroundColor = 
    # secondaryBackgroundColor =
    # textColor = 
    # font = 
    ```
    
    Sets the theming for your Streamlit app.  `base` can be `"dark"` or `"light"`.
    All the other options set specific colors.
    
    
    # My usual config
    
    My typical config is pretty simple.  I use most of the default settings.
    
    ```toml
    [browser]
    serverAddress = "127.0.0.1"
    gatherUsageStatistics = false
    
    [runner]
    enableMagic = false
    
    [theme]
    base = "dark"
    ```
    """
    )
