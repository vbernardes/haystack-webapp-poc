import os
import requests
import streamlit as st

HAYSTACK_URL = os.getenv('HAYSTACK_QA_URL', 'http://localhost:8000')


st.write('# Question Answering')

st.text_input('What do you want to know?', key='query')
query = st.session_state.query

if query:
    haystack_query_url = f'{HAYSTACK_URL}/query'
    response = requests.post(haystack_query_url, json={'query': query})
    response_json = response.json()

    st.write('### Extracted answers')
    score_threshold = .75
    valid_answers = []
    for answer in response_json.get('answers'):
        if answer.get('score') >= score_threshold:
            valid_answers.append(answer)

    if not valid_answers:
        st.write('No answers found.')
    else:
        for answer in valid_answers:
            st.write(f'''**Answer**: {answer.get('answer')}''')
            st.write(f'''**Score**: {answer.get('score'):.2f}''')
            st.write(f'''**Context**: {answer.get('context').strip()}''')
            st.write('---')
