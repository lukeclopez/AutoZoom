import tkinter as tk
import tkinter.font as font

from main import main as script

WIDTH = 900
HEIGHT = 500


class Window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry(f"{WIDTH}x{HEIGHT}")
        self.window.attributes("-fullscreen", True)
        self.fullScreenState = False
        self.window.bind("<F11>", self.toggle_full_screen)
        self.window.bind("<Escape>", self.quit_full_screen)

        large_font = font.Font(size=150)

        self.entry = tk.Entry(
            self.window,
            font=large_font
        )
        self.entry.pack()
        self.entry.focus_set()

        tk.Button(
            self.window,
            font=large_font,
            text="Join",
            command=lambda: script(*self.entry.get().split(" "))
        ).pack()

        self.window.mainloop()

    def toggle_full_screen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quit_full_screen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)


if __name__ == '__main__':
    app = Window()
