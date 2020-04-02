import tkinter as tk
import tkinter.font as font

from main import main as script


class Window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.state("zoomed")
        self.window.bind("<Escape>", quit)

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


if __name__ == '__main__':
    app = Window()
