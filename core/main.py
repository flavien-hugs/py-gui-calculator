import tkinter as tk

from .constants import Color, FontStyle


class Calculator:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("unsta.inc calculator")

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()

        self.total_label, self.current_label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 1), '.': (4, 2)
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
        self.create_square_button()
        self.create_sqrt_button()

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

    def append_current_expression(self, value):
        self.current_expression += str(value)
        self.update_current_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(
                self.buttons_frame, text=str(digit),
                bg=Color.COLOR_WITH, fg=Color.COLOR_LABEL,
                font=FontStyle.DIGIT_FONT_STYLE, borderwidth=0,
                command=lambda x=digit: self.append_current_expression(x))

            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_current_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operators.items():
            button = tk.Button(
                self.buttons_frame, text=symbol,
                bg=Color.COLOR_OFF_WITH, fg=Color.COLOR_LABEL,
                font=FontStyle.DEFAULT_FONT_STYLE, borderwidth=0,
                command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear_window(self):
        self.total_expression = ""
        self.current_expression = ""
        self.update_total_label()
        self.update_current_label()

    def create_clear_button(self):
        clear_button = tk.Button(
            self.buttons_frame, text="C",
            bg=Color.COLOR_OFF_WITH, fg=Color.COLOR_LABEL,
            font=FontStyle.DEFAULT_FONT_STYLE, borderwidth=0,
            command=self.clear_window)
        clear_button.grid(row=0, column=1, sticky=tk.NSEW)

    def square(self):
        if self.current_expression:
            self.current_expression = eval(f"{self.current_expression}**2")
            self.update_current_label()

    def create_square_button(self):
        square_button = tk.Button(
            self.buttons_frame, text="x\u00b2",
            bg=Color.COLOR_OFF_WITH, fg=Color.COLOR_LABEL,
            font=FontStyle.DEFAULT_FONT_STYLE, borderwidth=0,
            command=lambda: self.square())
        square_button.grid(row=0, column=2, sticky=tk.NSEW)

    def sqrt(self):
        if self.current_expression:
            self.current_expression = eval(f"{self.current_expression}**0.5")
            self.update_current_label()

    def create_sqrt_button(self):
        sqrt_button = tk.Button(
            self.buttons_frame, text="\u221ax",
            bg=Color.COLOR_OFF_WITH, fg=Color.COLOR_LABEL,
            font=FontStyle.DEFAULT_FONT_STYLE, borderwidth=0,
            command=lambda: self.sqrt())
        sqrt_button.grid(row=0, column=3, sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()

        self.current_expression = str(eval(self.total_expression))
        self.total_expression = ""
        self.update_current_label()

    def create_equals_button(self):
        equal_button = tk.Button(
            self.buttons_frame, text="=",
            bg=Color.COLOR_RED, fg=Color.COLOR_LABEL,
            font=FontStyle.DEFAULT_FONT_STYLE, borderwidth=0,
            command=self.evaluate)
        equal_button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        expresssion = self.total_expression
        for operator, symbol in self.operators.items():
            expresssion = expresssion.replace(operator, f"{symbol}")
        self.total_label.config(text=expresssion)

    def update_current_label(self):
        self.current_label.config(text=self.current_expression[:11])

    def run(self):
        self.window.mainloop()
