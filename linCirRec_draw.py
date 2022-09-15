import tkinter as tk
from turtle import update
import globals
import cv2
import popup


def into_drawing_mode():
    global canvas
    canvas = globals.canvas
    global mode_num
    mode_num = popup.popup_drawing()
    
    canvas.bind('<Button>', star_draw)
    canvas.bind('<ButtonRelease>', end_draw)
    
def star_draw(event):
    global x_star, y_star
    x_star = event.x
    y_star = event.y

def end_draw(event):
    x_end = event.x
    y_end = event.y
    color = (0, 0, 0)
    img = globals.img
    if mode_num == 1:
        #canvas.create_line(x_star, y_star, x_end, y_end, fill="#fb0")
        cv2.line(img,(x_star, y_star),(x_end,y_end),color, 1)
    elif mode_num == 2:
        cv2.ellipse(img,(int((x_star+x_end)/2), int((y_star+y_end)/2)),
                    (int(abs(x_star-x_end)/2), int(abs(y_star-y_end)/2)),
                    0, 0, 360, color, 1)
    elif mode_num == 3:
        cv2.rectangle(img,(x_star, y_star),(x_end, y_end),color, 1)
    globals.update_canvas(img)



"""
If use pyhton3 linCirRec_draw.py, we can test this function, without going through the main GUI operation
"""
if __name__ == "__main__":
    canvas = globals.canvas
    canvas.pack(side= tk.TOP)
    path = '/Users/natsu/Documents/ProgrammingProject/py-img-editor/img/Jump.jpg'
    img = cv2.imread(cv2.samples.findFile(path), cv2.IMREAD_UNCHANGED)
    globals.update_canvas(img)
    height, width, no_channels = img.shape
    canvas.config(width = width, height = height)
    into_drawing_mode()
    globals.window.mainloop()