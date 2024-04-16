from openai import OpenAI
import streamlit as st

f = open("keys/.openai_api_key.txt")
key = f.read()
client = OpenAI(api_key)
st.snow()
st.title("GenAI Code Reviwer]")
st.header('MCQ GENERATOR APP')

prompt = st.text_input('Paste Your Code Here')
if st.button("Review Code"):
    st.balloons()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        
    )

    if response.choices:
        st.write(response.choices[0].message.content)