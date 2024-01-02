import streamlit as st
v = False
st.set_page_config(page_title="fase 2")
st.write("meu [tik tok](https://www.tiktok.com/@somente.3?lang=pt-BR)")
st.write("parabéns")
st.title("fase2")
st.subheader("អាជ្ញាប័ណ្ណសាធារណៈទូទៅរបស់ GNU")
if st.chat_input("resposta") == "audacity":
    v = True
if v == True:
    st.subheader("[fase 3](https://fase3-enigma3.streamlit.app)")
