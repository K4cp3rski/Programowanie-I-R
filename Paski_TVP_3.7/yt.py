import youtube_dl
import os
from converter import Converter


def konwertuj(nazwa):
    conv = Converter()

    filename = nazwa
    out_name = "tmp.mp4"

    os.system(f'ffmpeg -i {filename} {out_name}')


def dl(link):
    ydl_opts = {"outtmpl": "dl"}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        vid = ydl.download([link])


def main(link):
    if not os.path.exists("dl.ismv"):
        dl(link)
        konwertuj("dl.ismv")


if __name__ == "__main__":
    ref = 'https://www.tvp.info/54233992/raport-o-koronawirusie-8-czerwca?copyId=54146645%27'
    main(ref)
