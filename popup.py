import streamlit as st
from streamlit_modal import Modal

modal = Modal(key="Demo Key",title="Test")

for col in st.columns(8):
    
    with col:
        open_modal = st.button(label='Button')
        if open_modal:
            with modal.container():
                st.markdown('Test Popup Window')