"""
Create GUI with Tkinter for the software that we are designing.
"""
from email.mime import image
from gc import callbacks
from importlib.resources import path
from PIL import Image, ImageTk
import cv2
from pickle import FRAME
import tkinter as tk
from turtle import fillcolor, left
from matplotlib.pyplot import text
import numpy
import globals
from fillingColor import filling



def main():    
    # Create an instance of Tkinter's Tk class. assign it to window variables.
    global window
    window = tk.Tk()
    # Create Title Label
    window.title("Image Editor")
    frame = tk.Frame(window)
    frame.pack(side = tk.TOP)
    global canvas
    canvas = tk.Canvas(window, height= 20)
    globals.set_canvas(canvas)
    canvas.pack(side= tk.TOP)
    # Entry is ready to output the address 
    entryInput = tk.Entry(frame, width = 60, text="the absolute path of Img with suffix")
    # the default value so we delete later
    entryInput.insert(0, "/Users/natsu/Documents/ProgrammingProject/py-img-editor/img/Jump.jpg")
    
    # Create a button for loading images.
    loadImgButton = tk.Button(
        frame,
        text="Load Img",
        bg="white",
        fg="black",
    # once load button got clicked, loadIMG image to the path
        command=lambda:loadIMG(entryInput.get())
    )
    
    save_button = tk.Button(
        frame,
        text="Save Img",
        bg="white",
        fg="black",
        # once save button got clicked, save the image to the path
        command=lambda:saveIMG(entryInput.get())
    )
     
    #Load the loading Button onto the Gui
    # Create a label for the GUI that is related to the entry;
    msg = tk.Label(frame, text="Input the Path you to Load or Save")
    #Create an entry so that when the user enters an string of text, it becomes the name of the output file.(AFTER EDIT:)
    #Create a button for collecting the entryInput name:
    msg.pack(side=tk.LEFT)
    entryInput.pack(side = tk.LEFT)
    loadImgButton.pack(side=tk.LEFT)
    save_button.pack(side = tk.LEFT)
    
    window.mainloop()

def operation_side():
        operation_frame = tk.Frame(window)
        operation_frame.pack(side = tk.BOTTOM)
        create_button_in_operation(operation_frame, "Filling Color",filling)
        # for fillingColor function, you have to enter the coordinate in terminal, and # filling color is fixed with purple, this will be optimized in the # future
        create_button_in_operation(operation_frame, 1, print(2))
        #
        #       IMPORTANT! PLEASE READ THIS,  BY XIAOXIA
        #       
        #       1.if after you implement your function, you see color got inverse or may not. Because Image.fromarray() will inverse color, but at some point it reverse back by cvtColor, don't worry if showing wrong color, it will be fixed at high-level
        #
        #       2. My way is to have no para in the function, then import img from globals.py to process, just recommend.
        #
        #       3. if you wanna use the same way as me, import img from globals.py, and globals.update_canvas(img_after_change) in the end will be fine. More illustrates and comments is in the fillingColor
        #
        #
        create_button_in_operation(operation_frame, 2, print(3))
        create_button_in_operation(operation_frame, 3, print(4))
        create_button_in_operation(operation_frame, 4, print(5))
        create_button_in_operation(operation_frame, 5, print(6))
        create_button_in_operation(operation_frame, 6, print(7))
        create_button_in_operation(operation_frame, 7, print(8))
    
def loadIMG(path):
    try:
        global img
        # load new image
        globals.img = cv2.imread(cv2.samples.findFile(path), cv2.IMREAD_UNCHANGED)
        img = globals.img
        globals.change_img(globals.img)
        height, width, no_channels = img.shape
        # Image.fromarray() will inverse color, here we change back
        img_convert = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # to make the save size as image
        canvas.config(width = width, height = height)
        globals.update_canvas(img_convert)
        # as the img shows, function buttom will show up
        operation_side()
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
    try:
        cv2.imwrite(path, img)
        tk.messagebox.showinfo(title="Image Saved", message="Image Successfully saved in " + path )
    except cv2.error as e:
        tk.messagebox.showwarning(title="No suffix or Wrong Path", message= "You May Need To Have Suffix, Such As .jpg or .png")
    except NameError:
        tk.messagebox.showwarning(title="No Image Loaded Yet", message= "You Have To Have Image To Save")

def create_button_in_operation(fra, fun_name,fun,):
    tk.Button(
        fra,
        width= 8,
        height= 2,
        text=fun_name,
        bg="white",
        fg="black",
        command=lambda:fun()
    ).pack(side= tk.LEFT)
    
    

if __name__ == "__main__":
    main()