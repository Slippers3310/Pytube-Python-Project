import streamlit as st
import pytube

url = st.text_input(" Lütfen indireceğiniz video adresini yazın")

if len(url) > 0:

    sonuc=pytube.YouTube(url).streams.first().download()

    import streamlit as st

    with open(sonuc, "rb") as file:
        btn = st.download_button(
                label="Download image",
                data=file,
                file_name="video.3gpp",
                mime="video/3gpp"
              )