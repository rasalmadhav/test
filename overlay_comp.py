import streamlit as st
from streamlit_modal import Modal

# Create a layout with two columns
sidebar_col, empty_col, main_col = st.columns([1, 2, 4])

# Sidebar content
with sidebar_col:
    # Add your sidebar elements here
    st.sidebar.header("Sidebar")
    st.sidebar.button("Sidebar Button")

# Main content including the modal
with main_col:
    st.title("Main Content")
    st.write("Main content goes here")

    # Create and display the modal
    with Modal():
        st.header("Modal")
        st.write("Modal content goes here")
        st.button("Close Modal")