import tkinter as tk

from .constants import Color, FontStyle


class Calculator:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("unsta.inc calculator")

        self.total_expression = "0"
        self.current_expression = "0"

        self.display_frame = self.create_display_frame()
        self.total_label = self.create_display_labels()
        self.buttons_frame = self.create_buttons_frame()

    def create_display_labels(self):
        total_label = tk.Label(
            self.display_frame,
            text=self.total_expression, anchor=tk.E,
            bg=Color.COLOR_LIGHT_GRAY, fg=Color.COLOR_LABEL,
            padx=24, font=FontStyle.SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill="both")

        current_label = tk.Label(
            self.display_frame,
            text=self.current_expression, anchor=tk.E,
            bg=Color.COLOR_LIGHT_GRAY, fg=Color.COLOR_LABEL,
            padx=24, font=FontStyle.LARGE_FONT_STYLE)
        current_label.pack(expand=True, fill="both")

        return total_label, current_label

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
