import tkinter as tk
import tkinter.font as font

from main import main as script


class Window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.state("zoomed")
        self.window.configure(bg="#6e7b8f")
        self.window.bind(
            "<Return>",
            lambda x: script(*self.entry.get().split(" "))
        )

        large_font = font.Font(size=75)

        self.entry = tk.Entry(
            self.window,
            font=large_font,
            width=16
        )
        self.entry.grid(padx=50, pady=50)
        self.entry.focus_set()

        tk.Button(
            self.window,
            font=large_font,
            text="Join",
            command=lambda: script(*self.entry.get().split(" "))
        ).grid(row=1, padx=50, pady=50)

        self.window.mainloop()


if __name__ == '__main__':
    app = Window()
