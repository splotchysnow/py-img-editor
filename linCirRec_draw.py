import tkinter as tk
from globals import update_canvas, operation_frame, window, canvas
import globals
import cv2
import popup


def into_drawing_mode():
    global mode_num, color, thick
    mode_num = popup.popup_drawing()
    color = popup.color
    thick = int(popup.thick)
    global press_S_to_stop_label
    press_S_to_stop_label = tk.Label(window, font=("Arial", 25),text="Press S to stop Drawing")
    hide_other()
    canvas.bind('<Button>', star_draw)
    canvas.bind('<ButtonRelease>', end_draw)
    window.bind('<Key>', stop_drawing)
    
def star_draw(event):
    global x_star, y_star
    x_star = event.x
    y_star = event.y

def end_draw(event):
    x_end = event.x
    y_end = event.y
    img = globals.img
    if mode_num == 1:
        #canvas.create_line(x_star, y_star, x_end, y_end, fill="#fb0")
        cv2.line(img,(x_star, y_star),(x_end,y_end),color, thick)
    elif mode_num == 2:
        cv2.ellipse(img,(int((x_star+x_end)/2), int((y_star+y_end)/2)),
                    (int(abs(x_star-x_end)/2), int(abs(y_star-y_end)/2)),
                    0, 0, 360, color, thick)
    elif mode_num == 3:
        cv2.rectangle(img,(x_star, y_star),(x_end, y_end),color, thick)
    update_canvas(img)

def stop_drawing(event):
    if(event.char == 's' or event.char == 'S'):
        canvas.unbind('<Button>')
        canvas.unbind('<ButtonRelease>')
        press_S_to_stop_label.destroy()
        operation_frame.pack()


def hide_other():
    operation_frame.pack_forget()
    press_S_to_stop_label.pack()


"""
If use pyhton3 linCirRec_draw.py, we can test this function, without going through the main GUI operation
"""
if __name__ == "__main__":
    canvas.pack(side= tk.TOP)
    path = 'img/Jump.jpg'
    img = cv2.imread(cv2.samples.findFile(path), cv2.IMREAD_UNCHANGED)
    globals.img = img
    update_canvas(img)
    height, width, no_channels = img.shape
    canvas.config(width = width, height = height)
    into_drawing_mode()
    window.mainloop()