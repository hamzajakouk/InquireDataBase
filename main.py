import streamlit as st
from kick_it import get_question , create_vectore
st.title("tryme 📫📫")
start = st.button("give you sources")

if start :
    pass
question = st.text_input("Let's Kick it")

if question:
    chain = get_question()
    st.header("Answer")
    st.write(chain(question)["result"])