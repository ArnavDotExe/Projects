import streamlit as st
from pytube import YouTube

def download_video(url, path):
    try:
        st.write("Downloading video...")
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download(path)
        st.write("Video downloaded successfully!")
    except Exception as e:
        st.write("An error occurred:", str(e))

def main():
    st.title("YouTube Video Downloader")
    st.write("Enter the YouTube video URL and choose a download location.")

    url = st.text_input("Video URL")
    path = st.text_input("Download Location", "/path/to/save/video")

    if st.button("Download"):
        download_video(url, path)

if __name__ == "__main__":
    main()