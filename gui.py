import tkinter as tk
import tkinter.font as font

from main import main as script

WIDTH = 900
HEIGHT = 500


class Window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry(f"{WIDTH}x{HEIGHT}")

        large_font = font.Font(size=200)

        tk.Button(
            self.window,
            font=large_font,
            text="Join",
            command=script
        ).pack()

        self.window.mainloop()


if __name__ == '__main__':
    app = Window()
