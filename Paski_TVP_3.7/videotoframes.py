import cv2
import os
import shutil


def video_wrapper(name, fps=5):
    vidcap = cv2.VideoCapture(str(name))
    try:
        os.mkdir("./movie_tmp")
    except FileExistsError:
        shutil.rmtree("./movie_tmp")
        os.mkdir("./movie_tmp")

    def getFrame(sec):
        vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
        hasFrames, image = vidcap.read()
        if hasFrames:
            cv2.imwrite(f"movie_tmp/image"+str(count)+".jpg", image)     # save frame as JPG file
        return hasFrames
    sec = 10
    beg = sec
    frameRate = fps  # it will capture image every fps seconds
    count = 1
    success = getFrame(sec)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec)
    # print(f"Numer ostatniej klatki to: {(sec-beg)/frameRate}")
    return int((sec-beg)/frameRate)

