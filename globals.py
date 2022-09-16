"""_summary_: Used for global functions and declarations."""

import tkinter as tk
from PIL import Image, ImageTk
from cv2 import cvtColor, COLOR_BGR2RGB

# this global is not important, saying window here only for convinient
window = tk.Tk()
window.title("Image Editor")
# img to control the real data of picture we process
img = None

# canvas is where we display
canvas = tk.Canvas(window, height= 20)

# the one to hold the button
operation_frame = tk.Frame(window)

# To update the canvas for the frontend
def update_canvas(image):
    global photo
    photo = ImageTk.PhotoImage(image = Image.fromarray(cvtColor(image, COLOR_BGR2RGB)))
    canvas.create_image(0, 0, image=photo, anchor=tk.NW)