import streamlit as st
import pytube

url = st.text_input(" Lütfen indireceğiniz video adresini yazın")

if len(url) > 0:
    # Create a YouTube object
    yt = pytube.YouTube(url)

    # Get the best available stream for both video and audio
    best_stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
    f = best_stream.download()

    with open(f, "rb") as file:
      btn = st.download_button(
                  label="Download image",
                  data=file,
                  file_name="video.mp4",
                  mime="video/mp4"
                )