import os
import requests
import streamlit as st

HAYSTACK_URL = os.getenv('HAYSTACK_URL', 'http://localhost:8000')


st.sidebar.write()

st.text_input('What do you want to know?', key='query')
query = st.session_state.query

haystack_query_url = f'{HAYSTACK_URL}/query'
response = requests.post(haystack_query_url, json={'query': query})

st.write(f'Response code: {response}')
st.write(response.json())
