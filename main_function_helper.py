
import cv2
import tkinter as tk
from globals import *
import globals
from fillingColor import filling
from linCirRec_draw import into_drawing_mode

def quit(event):
    """_summary_ Kill the GUI windows
    Args:
        event (_type_): _description_ takes and events arguments
    """
    window.destroy()

def loadIMG(path):
    """_summary_ Load the image through the path with the help of the global.py script

    Args:
        path (_type_): _description_ path of the image being imported.
    """
    try:
        global img
        # load new image
        img = cv2.imread(cv2.samples.findFile(path), cv2.IMREAD_UNCHANGED)
        globals.img = img
        # globals.change_img(globals.img)
        height, width, no_channels = img.shape
        # Image.fromarray() will inverse color, here we change back
        # to make the save size as image
        canvas.config(width = width, height = height)
        update_canvas(img)
        # as the img shows, function buttom will show up
        operation_frame.pack(side = tk.BOTTOM)
    except(FileNotFoundError):
        # the case that path is wrong
        wrong_path = "Doesn't exist image in the path \"" + path + "\""
        tk.messagebox.showwarning(title="Wrong Path", message=wrong_path)
    except:
        # for some reason we don't know, some picture cannot be processing,
        # even they are .jpg just as others
        tk.messagebox.showwarning(title="Not Applicable", message="This img is not applicable")
    # it will give AttributeError: module 'tkinter' has no attribute 'update', but we can just ignor it
    
def saveIMG(path):
    """_summary_: saves image to the path.

    Args:
        path (_type_): _description_
    """
    try:
        cv2.imwrite(path, img)
        tk.messagebox.showinfo(title="Image Saved", message="Image Successfully saved in " + path )
    except cv2.error as e:
        tk.messagebox.showwarning(title="No suffix or Wrong Path", message= "You May Need To Have Suffix, Such As .jpg or .png")
    except NameError:
        tk.messagebox.showwarning(title="No Image Loaded Yet", message= "You Have To Have Image To Save")

def operation_side():
    # Grabs the gloabl's frame containers to gather all the buttons.
    # operation_frame = globals.operation_frame

    # Creates all the nessiary buttons.
    create_button_in_operation(operation_frame, "Filling Color", filling)
    # for fillingColor function, you have to enter the coordinate in terminal, and # filling color is fixed with purple, this will be optimized in the # future
    create_button_in_operation(operation_frame, "Drawing", into_drawing_mode)
    
    """
           IMPORTANT! PLEASE READ THIS,  BY XIAOXIA
           
           1.if after you implement your function, you see color got inverse or may not. Because Image.fromarray() will inverse color, but at some point it reverse back by cvtColor, don't worry if showing wrong color, it will be fixed at high-level
    
           2. My way is to have no para in the function, then import img from globals.py to process, just recommend.
    
           3. if you wanna use the same way as me, import img from globals.py, and globals.update_canvas(img_after_change) in the end will be fine. More illustrates and comments is in the fillingColor
    """
    create_button_in_operation(operation_frame, 2, print(3))
    create_button_in_operation(operation_frame, 3, print(4))
    create_button_in_operation(operation_frame, 4, print(5))
    create_button_in_operation(operation_frame, 5, print(6))
    create_button_in_operation(operation_frame, 6, print(7))
    create_button_in_operation(operation_frame, 7, print(8))

def create_button_in_operation(fra, fun_name,fun,):
    """_summary_ Create a button, store it in the frame, gives the button a name.
    Args:
        fra (_type_): _description_  : stores the button into it's correct frames.
        fun_name (_type_): _description_ gives the button a name
        fun (_type_): _description_ : for debugging
    """
    tk.Button(
        fra,
        width= 8,
        height= 2,
        text=fun_name,
        bg="white",
        fg="black",
        command=lambda:fun()
    ).pack(side= tk.LEFT)
