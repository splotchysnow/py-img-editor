from curses import window
from tkinter import TOP
import globals
import tk
import cv2


def into_drawing_mode():
    canvas = globals.canvas
    
    canvas.bind('<Button>',star_draw)
    canvas.bind('<ButtonRelease>', end_draw)
    
def star_draw(event):
    global x_star, y_star
    x_star = event.x
    y_star = event.y

def end_draw(event):
    x_end = event.x
    y_end = event.y
    canvas.create_rectangle(x_star, y_star, x_end, y_end,
    outline="#fb0", fill="#fb0")


if __name__ == "__main__":
    canvas = globals.canvas
    canvas.pack(side= TOP)
    path = '/Users/natsu/Documents/ProgrammingProject/py-img-editor/img/Jump.jpg'
    img = cv2.imread(cv2.samples.findFile(path), cv2.IMREAD_UNCHANGED)
    globals.update_canvas(img)
    height, width, no_channels = img.shape
    canvas.config(width = width, height = height)
    into_drawing_mode()
    globals.window.mainloop()