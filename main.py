import pyautogui as pag
import psutil
import os

ZOOM_PATH = r"C:\Users\xluca\AppData\Roaming\Zoom\bin\Zoom.exe"
MEETING_ID = os.getenv("MEETING_ID")
MEETING_PASSWORD = os.getenv("MEETING_PASSWORD")


def main():
    open_zoom()
    find_and_click_center("join.png")
    move_mouse_out_of_way()
    find_and_click_center("enter-meeting-id.png")
    pag.write(MEETING_ID)
    find_and_click_center("join-after-meeting-id.png")
    find_and_click_center("enter-meeting-password.png")
    pag.write(MEETING_PASSWORD)
    find_and_click_center("join-meeting-after-password.png")


def move_mouse_out_of_way():
    pag.moveTo(100, 200)


def find_and_click_center(image):
    loc = None
    while loc == None:
        loc = pag.locateCenterOnScreen("images/" + image, confidence=0.9)
    x, y = loc
    pag.click(x=x, y=y)


def open_zoom():
    psutil.Popen([ZOOM_PATH])


if __name__ == "__main__":
    main()
