import pyautogui as pag
import psutil
import time
import json
import os


def main(meeting_id, meeting_password):
    with open("data/path.txt") as f:
        zoom_path = f.read()

    open_zoom(zoom_path)
    time.sleep(3)
    pag.press('tab')
    pag.press('enter')
    time.sleep(3)
    pag.write(meeting_id)
    for x in range(6):
        pag.press('tab')
    pag.press('enter')
    time.sleep(3)
    pag.write(meeting_password)
    pag.press('tab')
    pag.press('enter')


def open_zoom(path):
    psutil.Popen([path])


if __name__ == "__main__":
    main(input("ID: "), input("PW: "))
