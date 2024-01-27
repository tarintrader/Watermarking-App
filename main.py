from datetime import datetime
from tkinter import *
from tkinter import ttk, filedialog
from pillow import Image, ImageDraw, ImageFont
from popups import PopupTextOptions, PopupLogoOptions
from pillow import AddWaterMark
import os

YELLOW = "#f7f5dd"

text_options = None
logo_options = None


def upload_img(event=None):
    global img_path
    f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]
    img_path = filedialog.askopenfilename(filetypes=f_types)
    print('Selected:', img_path)
    img_button.configure(style="TButton.FileSelected.TButton", text="Image ✔")


def add_text(event=None):
    global img_path, text_options

    # Open a new window using the PopupWindow class
    text_options = PopupTextOptions(window)
    text_button.configure(style="TButton.FileSelected.TButton", text="Text ✔")


def upload_logo(event=None):
    global logo_path, logo_options
    f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]
    logo_path = filedialog.askopenfilename(filetypes=f_types)
    print('Selected:', logo_path)
    logo_button.configure(style="TButton.FileSelected.TButton", text="Logo ✔")

    # Open a new window using the PopupWindow class
    logo_options = PopupLogoOptions(window)


def add_text_with_transparency(img, text, font, font_size, color, transparency):
    # Create a new image with an RGBA mode
    txt = Image.new('RGBA', img.size, (0, 0, 0, 0))

    # Draw the text on the new image
    draw = ImageDraw.Draw(txt)
    text_width = draw.textlength(text, font=font)
    # text_height = font.getsize(text)[1]

    # Calculate the position to center the text
    position = (
        (img.width - text_width) // 2,
        (img.height - font_size) // 2
    )

    draw.text(position, text, font=font, fill=color)

    # Separate the alpha channel from the text image
    txt_alpha = txt.split()[3]

    # Apply transparency to the alpha channel
    txt_alpha = txt_alpha.point(lambda p: p * transparency)

    # Paste the text image with the modified alpha channel onto the original image
    result = Image.alpha_composite(img.convert("RGBA"), txt.convert("RGBA"))

    return result


def save(event=None):
    img = Image.open(img_path).convert("RGBA")
    width_img, height_img = img.size
    center_x, center_y = (int(width_img / 2), int(height_img / 2))

    if text_options and text_options.watermark:
        alpha = int(255 * (1 - text_options.transparency / 10))
        color_mapping = {
            "white": (255, 255, 255, alpha),
            "black": (0, 0, 0, alpha),
            "red": (255, 0, 0, alpha),
            "green": (0, 255, 0, alpha),
            "blue": (0, 0, 255, alpha),
            "yellow": (255, 255, 0, alpha)
        }
        color_tuple = color_mapping.get(text_options.color)
        font = ImageFont.truetype("impact.ttf", text_options.size * 20)
        font_size = text_options.size * 20
        print("Font Size:", font_size)

        result_image = add_text_with_transparency(
            img,
            text_options.text,
            font,
            font_size,
            color_tuple,
            text_options.transparency
        )

        # Get the user's desktop path
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

        # Create a folder named "WaterMarking App" on the desktop if it doesn't exist
        watermarking_app_folder = os.path.join(desktop_path, "WaterMarking App")
        os.makedirs(watermarking_app_folder, exist_ok=True)

        # Construct the filename with a timestamp to avoid overwriting
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        result_image_filename = f"result_image_{timestamp}.png"

        # Construct the full path for saving the modified image inside the folder
        result_image_path = os.path.join(watermarking_app_folder, result_image_filename)

        result_image.save(result_image_path)  # Save the modified image to the "WaterMarking App" folder




    elif logo_options and logo_options.watermark:
        logo = Image.open(logo_path).convert("RGBA")
        logo_size = (logo_options.size * 100, logo_options.size * 100)
        logo.thumbnail(logo_size)
        width_logo, height_logo = logo.size
        logo_x = int(center_x - (width_logo / 2))
        logo_y = int(center_y - (height_logo / 2))
        alpha = int(255 * (1 - logo_options.transparency / 10))

        data = logo.getdata()
        new_data = [(r, g, b, alpha) for r, g, b, a in data]
        logo.putdata(new_data)

        img.paste(logo, (logo_x, logo_y), logo)

        # Get the user's desktop path
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

        # Create a folder named "WaterMarking App" on the desktop if it doesn't exist
        watermarking_app_folder = os.path.join(desktop_path, "WaterMarking App")
        os.makedirs(watermarking_app_folder, exist_ok=True)

        # Construct the full path for saving the modified image inside the folder
        result_image_path = os.path.join(watermarking_app_folder, "result_image.png")

        img.save(result_image_path)  # Save the modified image to the "WaterMarking App" folder



# ------------------------------- INTERFACE ------------------------------- #


window = Tk()
window.title("WaterMarking App")
window.config(padx=10, pady=50, bg=YELLOW)

window.iconbitmap("W.ico")

canvas = Canvas(width=500, height=112, bg="red", highlightthickness=0)
app_logo = PhotoImage(file="Watermarking App.png")
canvas.create_image(250, 66, image=app_logo)
canvas.grid(column=0, row=1, columnspan=6, pady=30, padx=15)

img_button = ttk.Button(text='Select Image', command=upload_img)
img_button.grid(column=1, row=2)
text_button = ttk.Button(text="Add Text", command=add_text)
text_button.grid(column=2, row=2)
logo_button = ttk.Button(text="Add Logo", command=upload_logo)
logo_button.grid(column=3, row=2)
save_button = ttk.Button(text="Save", command=save)
save_button.grid(column=4, row=2)

window.mainloop()

# ------------------------------- EDIT FILE ------------------------------- #
