import tkinter as tk


LIGHT_GRAY = "#ECF2FF"
LABEL_ORANGE = "#F99417"
DIGITS_BLUE = "#E4FBFF"
EQUALS_BLUE = "#8BF5FA"
OPERATORS_BLUE = "#CCF2F4"

TOTAL_LABEL_FONT = ("Georgia", 18, )
CURRENT_LABEL_FONT = ("Georgia", 35, "bold")
DIGITS_FONT = ("Georgia", 22, "bold")


class TkCalculator:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("350x650")
        self.root.resizable(None, None)
        self.root.title("Andr-E-Bacus")
        self.total_expression = "0"
        self.current_expression = "0"
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        self.total_label, self.current_label = self.create_display_labels()
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.digits_dictionary = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), ".": (4, 1)
        }

        self.operators_symbols = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.create_digits_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

    def create_display_frame(self):
        display_frame = tk.Frame(self.root, height=150, bg=LIGHT_GRAY)
        display_frame.pack(expand=True, fill="both")
        return display_frame

    def create_buttons_frame(self):
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(expand=True, fill="both")
        return buttons_frame

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, font=TOTAL_LABEL_FONT,
                               padx=20, bg=LIGHT_GRAY, fg=LABEL_ORANGE, anchor=tk.E)
        total_label.pack(expand=True, fill="both")
        current_label = tk.Label(self.display_frame, text=self.current_expression, font=CURRENT_LABEL_FONT,
                                 padx=20, bg=LIGHT_GRAY, fg=LABEL_ORANGE, anchor=tk.E)
        current_label.pack(expand=True, fill="both")
        return total_label, current_label

    def create_digits_buttons(self):
        for digit, grid_position in self.digits_dictionary.items():
            digit_button = tk.Button(self.buttons_frame, text=str(digit), font=DIGITS_FONT, bg=DIGITS_BLUE,
                                     fg=LABEL_ORANGE, borderwidth=0)
            digit_button.grid(row=grid_position[0], column=grid_position[1], sticky=tk.NSEW)

    def create_operator_buttons(self):
        n = 1
        for operator, symbol in self.operators_symbols.items():
            operator_button = tk.Button(self.buttons_frame, text=symbol, font=DIGITS_FONT,
                                        bg=OPERATORS_BLUE, fg=LABEL_ORANGE, borderwidth=0)
            operator_button.grid(row=n, column=4, sticky=tk.NSEW)
            n += 1

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_backspace_button()
        self.create_square_button()
        self.create_square_root_button()
        self.create_equals_button()

    def create_clear_button(self):
        clear_button = tk.Button(self.buttons_frame, text="C", font=DIGITS_FONT,
                                 bg=OPERATORS_BLUE, fg=LABEL_ORANGE, borderwidth=0)
        clear_button.grid(row=0, column=1, sticky=tk.NSEW)

    def create_backspace_button(self):
        backspace_button = tk.Button(self.buttons_frame, text=u"\u232B", font=DIGITS_FONT,
                                     bg=OPERATORS_BLUE, fg=LABEL_ORANGE, borderwidth=0)
        backspace_button.grid(row=0, column=2, sticky=tk.NSEW)

    def create_square_button(self):
        square_button = tk.Button(self.buttons_frame, text="x\u00b2", font=DIGITS_FONT,
                                       bg=OPERATORS_BLUE, fg=LABEL_ORANGE, borderwidth=0)
        square_button.grid(row=0, column=3, sticky=tk.NSEW)

    def create_square_root_button(self):
        sqrt_button = tk.Button(self.buttons_frame, text="\u221ax", font=DIGITS_FONT,
                                bg=OPERATORS_BLUE, fg=LABEL_ORANGE, borderwidth=0)
        sqrt_button.grid(row=0, column=4, sticky=tk.NSEW)

    def create_equals_button(self):
        equals_button = tk.Button(self.buttons_frame, text="=", font=DIGITS_FONT,
                                  bg=EQUALS_BLUE, fg=LABEL_ORANGE, borderwidth=0)
        equals_button.grid(row=4, column=3, sticky=tk.NSEW)

    def update_current_expression(self, value):
        self.current_expression += value
        self.update_current_label()

    def update_current_label(self):
        self.current_label.config(text=self.current_expression)

    def update_total_label(self):
        pass

    def run_calculator(self):
        self.root.mainloop()
