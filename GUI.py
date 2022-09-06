"""
Create GUI with Tkinter for the software that we are designing.
"""
from email.mime import image
from gc import callbacks
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
canvas.pack()

# Create an empty label.

entryInput = tk.Entry(frame, width = 60, text="the absolute path of Img with suffix")


def loadIMG():
    path = entryInput.get()
    try:
        img = cv2.cvtColor(cv2.imread(cv2.samples.findFile(path), cv2.IMREAD_UNCHANGED), cv2.COLOR_BGR2RGB)
    except(FileNotFoundError):
        # the case that path is wrong
        wrong_path = "Doesn't exist image in the path \"" + path + "\""
        tk.messagebox.showwarning(title="Wrong Path", message=wrong_path)
    except:
        # for some reason we don't know, some picture cannot be processing,
        # even they are .jpg just as others
        tk.messagebox.showwarning(title="Not Applicable", message="This img is not applicable")
        
    height, width, no_channels = img.shape
    photo = ImageTk.PhotoImage(image = Image.fromarray(img))
    canvas.config(width = width, height = height)
    canvas.create_image(0, 0, image=photo, anchor=tk.NW)
    tk.update()


# Create a button for loading images.
loadImgButton = tk.Button(
    frame,
    text="Load Img",
    bg="white",
    fg="black",
    # once load button got clicked, execute loadIMG function
    command=loadIMG
)

save_button = tk.Button(
    frame,
    text="Save Img",
    bg="white",
    fg="black",
    #command=saveIMG
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
