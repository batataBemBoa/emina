import streamlit as st
v = True
st.set_page_config(page_title="enigma somente.3")
st.write("meu [tik tok](https://www.tiktok.com/@somente.3?lang=pt-BR)")
st.subheader("bem-vindo ao meu enigma de somente 3 fases")
st.title("fase 1")
st.subheader("...bala")
st.subheader("ling???")
if st.chat_input("resposta") == "m":
    v = False
if v == False :
    st.write("[fase 2](https://fase2-enigma3.streamlit.app)")


