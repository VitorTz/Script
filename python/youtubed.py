from pytube import YouTube
from moviepy.editor import *
import os
import sys

""" 
Baixa um vídeo do youtube, converte em mp3 e salva no destino especificado
"""

def download_video(url, folder):
    # Cria a pasta se não existir
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Baixa o vídeo
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    video.download(folder)

    # Extrai o título do vídeo
    title = yt.title

    # Converte o vídeo em MP3 e salva na pasta
    video_path = os.path.join(folder, video.default_filename)
    mp3_path = os.path.join(folder, title + ".mp3")
    video_clip = AudioFileClip(video_path)
    video_clip.write_audiofile(mp3_path)
    video_clip.close()
    os.remove(video_path)

if __name__ == "__main__":
    url = sys.argv[1]
    folder = sys.argv[2]
    download_video(url, folder)
