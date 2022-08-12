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

        self.total_label, self.current_label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 1), '.': (4, 2), '%': (4, 3)
        }
        self.operators = {
            "/": "\u00F7", "*": "\u00D7",
            "-": "-", "+": "+"
        }
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)

        [
            (self.buttons_frame.rowconfigure(x, weight=1),
            self.buttons_frame.columnconfigure(x, weight=1)) for x in range(1, 5)
        ]

        self.create_digit_buttons()
        self.create_special_button()
        self.create_operator_buttons()

    def create_special_button(self):
        self.create_clear_button()
        self.create_equals_button()

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

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(
                self.buttons_frame, text=str(digit),
                bg=Color.COLOR_WITH, fg=Color.COLOR_LABEL,
                font=FontStyle.DIGIT_FONT_STYLE, borderwidth=0)

            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operators.items():
            button = tk.Button(
                self.buttons_frame, text=symbol,
                bg=Color.COLOR_OFF_WITH, fg=Color.COLOR_LABEL,
                font=FontStyle.DEFAULT_FONT_STYLE, borderwidth=0)
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_clear_button(self):
        clear_button = tk.Button(
            self.buttons_frame, text="C",
            bg=Color.COLOR_OFF_WITH, fg=Color.COLOR_LABEL,
            font=FontStyle.DEFAULT_FONT_STYLE, borderwidth=0)
        clear_button.grid(row=0, column=1, columnspan=3, sticky=tk.NSEW)

    def create_equals_button(self):
        equal_button = tk.Button(
            self.buttons_frame, text="=",
            bg=Color.COLOR_RED, fg=Color.COLOR_LABEL,
            font=FontStyle.DEFAULT_FONT_STYLE, borderwidth=0)
        equal_button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def run(self):
        self.window.mainloop()
