import tkinter as tk
import globals
import cv2
import popup


def into_drawing_mode():
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
    if mode_num == 1:
        canvas.create_line(x_star, y_star, x_end, y_end, fill="#fb0")
    elif mode_num == 2:
        canvas.create_oval(x_star, y_star, x_end, y_end, outline="#fb0", fill="#fb0")
    elif mode_num == 3:
        canvas.create_rectangle(x_star, y_star, x_end, y_end, outline="#fb0", fill="#fb0")
    


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