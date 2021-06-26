import os
import re
import shutil
if input("Czy zainstalować pakiety niezbędne do działania programu? (Skrypt zoptymalizowany pod system MacOs) "
         "[y/n]\n") == "y":
    os.system("pip install pytesseract")
    os.system("pip install opencv-contrib-python")
    os.system("pip install PythonVideoConverter")
    os.system("pip install youtube-dl")
    os.system("pip install alive_progress")
    if input("System MacOs? [y/n]?\n") == "y":
        os.system("brew install tesseract")
import pytesseract
import yt
from crop import get_cropped
from videotoframes import video_wrapper
import cleanup
from alive_progress import alive_bar
from time import sleep


def paski():
    # Przykładowy link: https://www.tvp.info/54233992/raport-o-koronawirusie-8-czerwca?copyId=54146645%27

    link = input("Proszę podać link do wydania TVP Info do Analizy:\n")
    fps = input("Z jaką dokładnością ma być przeanalizowany plik? (domyślnie 5 fps, mniej fps -> dłuższa analiza)\n")

    pytesseract.tesseract_cmd = r'/Users/k4cp3rskiii/.conda/envs/Paski_TVP_3.7/lib/python3.9/site-packages'

    # Podprogram odpowiadający za pobranie i konwersję pliku wideo do mp4
    yt.main(link)

    # Podprogram odpowiadający za pocięcie pliku wideo na klatki.
    # Liczba w wywołaniu funkcji jest opcjonalna, mówi co ile sekund jest wyciągana klatka
    num = video_wrapper("tmp.mp4", float(fps))

    # Część odpowiedzialna za przycinanie obrazka do samego paska z informacjami i zczytywania z niego tekstu
    print("Rozpoczynam analizę klatek...")
    frames = []
    with alive_bar(num) as bar:
        for i in range(1, num+1):
            sleep(0.03)
            bar()
            zdj = get_cropped(f"movie_tmp/image{i}.jpg")
            text = pytesseract.image_to_string(zdj, lang="pol")
            text = re.sub(r'[^\w\s]', '', text)
            frames.append(text)
            # print(text)
    print("Zakończono analizę klatek!")

    # Tutaj czyszczę odczytany tekst ze śmiecia
    frames = [cleanup.remove_punc(i) for i in frames]
    frames = [cleanup.remove_spaces(i) for i in frames]


    # Część odpowiedzialna za usunięcie powtórzeń ze zczytanych pasków
    new = cleanup.remove_repet(frames)

    os.remove("dl.ismv")
    os.remove("tmp.mp4")
    shutil.rmtree("./movie_tmp")

    print("Paski z tego wydania to:\n")
    for i in new:
        print(i)
        print("\n")

    with open("wynik.txt", "w") as f:
        for a in new:
            f.write(a)
            f.write("\n")


if __name__ == "__main__":
    paski()
