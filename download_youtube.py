from pytube import YouTube
import os

SAVE_PATH = "Download_data\\"

def download(url):

    yt = YouTube(url)
    yt.streams.filter(only_audio=True)

    stream = yt.streams.get_by_itag(22)
    stream.download(output_path=SAVE_PATH, filename='okey.mp3')