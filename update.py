from globals import canvas
from PIL import Image, ImageTk
import tkinter as tk



def update(new_image):
    global photo
    photo = ImageTk.PhotoImage(image = Image.fromarray(new_image))
    canvas(0, 0, image=photo, anchor=tk.NW)
    