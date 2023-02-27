import os
import requests
import streamlit as st

HAYSTACK_URL = os.getenv('HAYSTACK_DOC_RETRIEVAL_URL', 'http://localhost:8000')


st.write('# Document Retrieval')

st.text_input('What do you want to search about?', key='query')
query = st.session_state.query

if query:
    haystack_query_url = f'{HAYSTACK_URL}/query'
    response = requests.post(haystack_query_url, json={'query': query})
    response_json = response.json()

    st.write('### Retrieved documents')
    for doc in response_json.get('documents'):
        st.write(f'''{doc.get('content')}''')
        st.write('---')
