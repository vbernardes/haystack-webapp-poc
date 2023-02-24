import os
import requests
import streamlit as st

HAYSTACK_URL = os.getenv('HAYSTACK_URL', 'http://localhost:8000')


st.markdown('# Haystack PoC')

st.markdown('Please select an option from the sidebar on the left.')
