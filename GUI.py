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
from turtle import left
from matplotlib.pyplot import text
import numpy

# Create an instance of Tkinter's Tk class. assign it to window variables.
window = tk.Tk()

# Create Title Label
window.title("Image Editor")
    
frame = tk.Frame(window)
frame.pack(side = tk.TOP)
canvas = tk.Canvas(window)
canvas.pack(side= tk.BOTTOM)

# Create an empty label.

entryInput = tk.Entry(frame, width = 60, text="the absolute path of Img with suffix")

# the default value so we delete later
entryInput.insert(0, "/Users/natsu/Documents/ProgrammingProject/py-img-editor/img/Jump.jpg")
global img
def loadIMG(path):
    try:
        # load new image 
        img = cv2.imread(cv2.samples.findFile(path), cv2.IMREAD_UNCHANGED)
        height, width, no_channels = img.shape
    except(FileNotFoundError):
        # the case that path is wrong
        wrong_path = "Doesn't exist image in the path \"" + path + "\""
        return tk.messagebox.showwarning(title="Wrong Path", message=wrong_path)
    except:
        # for some reason we don't know, some picture cannot be processing,
        # even they are .jpg just as others
        return tk.messagebox.showwarning(title="Not Applicable", message="This img is not applicable")
    img_convert = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    global photo
    photo = ImageTk.PhotoImage(image = Image.fromarray(img_convert))
    canvas.config(width = width, height = height)
    canvas.create_image(0, 0, image=photo, anchor=tk.NW)
    # it will give AttributeError: module 'tkinter' has no attribute 'update', but we can just ignor it

def saveIMG():
    try:
        cv2.imwrite(path, img)
    except cv2.error as e:
        tk.messagebox.showwarning(title="No suffix or Wrong Path", message= "You May Need To Have Suffix, Such As .jpg or .png")
    except NameError:
        tk.messagebox.showwarning(title="No Image Loaded Yet", message= "You Have To Have Image To Save")
        



# Create a button for loading images.
loadImgButton = tk.Button(
    frame,
    text="Load Img",
    bg="white",
    fg="black",
    # once load button got clicked, execute loadIMG function
    command=lambda:loadIMG(entryInput.get())
)

save_button = tk.Button(
    frame,
    text="Save Img",
    bg="white",
    fg="black",
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

# Run the tkinter event loop. Method Listens for events.
window.mainloop()
