from pytube import YouTube
from pathlib import Path
import sys


download_path = Path("/mnt/HD/Vídeos")


def get_output_path(video: YouTube) -> Path:
    global download_path
    path = download_path / video.title
    return path


def download(link):
    video = YouTube(link)
    file = video.streams.get_highest_resolution()
    try:
        file.download(
            output_path=get_output_path(video),
            filename=video.title
        )
    except Exception as e:
        print(f"Não foi possível baixar o vídeo {video.title}. {e}")
    else:
        print(f"Download feito com sucesso! -> {video.title}")


def main() -> None:
    link = sys.argv[1]
    download(link)


if __name__ == "__main__":
    main()
