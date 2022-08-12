import tkinter as tk

from .constants import Color


class Calculator:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("unsta.inc calculator")

        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=Color.COLOR_LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def run(self):
        self.window.mainloop()
