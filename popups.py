from tkinter import *
from tkinter import ttk, filedialog

YELLOW = "#f7f5dd"


class PopupTextOptions:
    def __init__(self, parent):
        self.watermark = None
        self.window = Toplevel(parent)
        self.window.title("Options")

        # # Initialize attributes with default values or None
        # self.text_entry = None
        # self.color_var = StringVar()
        # self.color_var.set("white")  # Default color

        # Combobox for size selection
        self.size_var = StringVar()
        self.size_var.set("1")  # Default size
        self.size_combobox = ttk.Combobox(self.window, values=[str(i) for i in range(1, 11)])
        self.size_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.size_combobox.config(textvariable=self.size_var)

        # Combobox for transparency selection
        self.transparency_var = StringVar()
        self.transparency_var.set("0")  # Default transparency
        self.transparency_combobox = ttk.Combobox(self.window, values=[str(i) for i in range(11)])
        self.transparency_combobox.grid(row=2, column=1, padx=10, pady=10)
        self.transparency_combobox.config(textvariable=self.transparency_var)

        # Labels for Entry fields
        ttk.Label(self.window, text="Size:").grid(row=1, column=0, padx=10, pady=10)
        ttk.Label(self.window, text="Transparency:").grid(row=2, column=0, padx=10, pady=10)

        # Button to apply changes
        ttk.Button(self.window, text="Apply", command=self.apply_changes).grid(row=4, column=1, pady=10)

        # Entry fields for Text
        self.text_entry = Entry(self.window, width=30)
        self.text_entry.grid(row=0, column=1, padx=10, pady=10)

        # Combobox for color selection
        self.color_var = StringVar()
        self.color_var.set("black")  # Default color
        self.color_combobox = ttk.Combobox(self.window, values=["white", "black", "red", "green", "blue", "yellow"])
        self.color_combobox.grid(row=3, column=1, padx=10, pady=10)
        self.color_combobox.config(textvariable=self.color_var)

        # Labels for Entry fields
        ttk.Label(self.window, text="Text:").grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(self.window, text="Color:").grid(row=3, column=0, padx=10, pady=10)

    def apply_changes(self):
        # text = getattr(self, "text_entry", None)
        # if text:
        #     text = text.get()

        self.text = self.text_entry.get()
        self.size = int(self.size_var.get())
        self.transparency = int(self.transparency_var.get())
        self.color = self.color_var.get()

        self.watermark = True

        # Perform actions with the entered values (e.g., update the image with text, size, transparency, and color)
        print("Text:", self.text)
        print("Size:", self.size)
        print("Transparency:", self.transparency)
        print("Color:", self.color)
        self.window.destroy()


class PopupLogoOptions:
    def __init__(self, parent):
        self.logo_watermark = None
        self.window = Toplevel(parent)
        self.window.title("Options")

        # Combobox for size selection
        self.size_var = StringVar()
        self.size_var.set("1")  # Default size
        self.size_combobox = ttk.Combobox(self.window, values=[str(i) for i in range(1, 11)])
        self.size_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.size_combobox.config(textvariable=self.size_var)

        # Combobox for transparency selection
        self.transparency_var = StringVar()
        self.transparency_var.set("0")  # Default transparency
        self.transparency_combobox = ttk.Combobox(self.window, values=[str(i) for i in range(11)])
        self.transparency_combobox.grid(row=2, column=1, padx=10, pady=10)
        self.transparency_combobox.config(textvariable=self.transparency_var)

        # Labels for Entry fields
        ttk.Label(self.window, text="Size:").grid(row=1, column=0, padx=10, pady=10)
        ttk.Label(self.window, text="Transparency:").grid(row=2, column=0, padx=10, pady=10)

        # Button to apply changes
        ttk.Button(self.window, text="Apply", command=self.apply_changes).grid(row=4, column=1, pady=10)

    def apply_changes(self):
        self.size = int(self.size_var.get())
        self.transparency = int(self.transparency_var.get())

        self.watermark = True

        # Perform actions with the entered values (e.g., update the image with text, size, transparency, and color)
        print("Size:", self.size)
        print("Transparency:", self.transparency)
        self.window.destroy()
