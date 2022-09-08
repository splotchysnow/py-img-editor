import tkinter as tk
from PIL import Image, ImageTk

# this global is not important, saying window here only for convinient
window = None

# img to control the real data of picture we process
img = None

# canvas is where we display
canvas = None

# To update the img data in the backend
def change_img(image):
    global img
    img = image

# To update the canvas for the frontend
def update_canvas(image):
    global photo
    photo = ImageTk.PhotoImage(image = Image.fromarray(image))
    canvas.create_image(0, 0, image=photo, anchor=tk.NW)

# initial canvas
def set_canvas(can):
    global canvas
    canvas = can