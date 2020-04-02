import pyautogui as pag
import psutil
import time
import json
import os


def main(meeting_id, meeting_password):
    with open("data/path.txt") as f:
        zoom_path = f.read()

    open_zoom(zoom_path)
    find_and_click_center("join.png")
    move_mouse_out_of_way()
    find_and_click_center("enter-meeting-id.png")
    pag.write(meeting_id)
    find_and_click_center("join-after-meeting-id.png")
    find_and_click_center("enter-meeting-password.png")
    pag.write(meeting_password)
    find_and_click_center("join-meeting-after-password.png")


def move_mouse_out_of_way():
    pag.moveTo(100, 200)


def find_and_click_center(image, time_left=5):
    loc = None
    while loc == None and time_left > 0:
        loc = pag.locateCenterOnScreen("images/" + image, confidence=0.9)
        time_left -= 1

    if loc:
        x, y = loc
        pag.click(x=x, y=y)


def open_zoom(path):
    psutil.Popen([path])


if __name__ == "__main__":
    main(input("ID: "), input("PW: "))
