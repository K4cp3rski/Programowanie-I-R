import youtube_dl


def yt():
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        vid = ydl.download(['https://www.tvp.info/54233992/raport-o-koronawirusie-8-czerwca?copyId=54146645%27'])


def main():
    print("Hello World!")

    yt()


if __name__ == "__main__":
    main()


