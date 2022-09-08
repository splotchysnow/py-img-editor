import tkinter as tk
from PIL import Image, ImageTk

window = None
img = None
canvas = None
photo = None

def change_img(image):
    global img
    img = image
    
def update_canvas(image):
    global photo
    photo = ImageTk.PhotoImage(image = Image.fromarray(image))
    canvas.create_image(0, 0, image=photo, anchor=tk.NW)
    
def set_canvas(can):
    global canvas
    canvas = can