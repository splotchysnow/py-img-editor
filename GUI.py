"""
Create GUI with Tkinter for the software that we are designing.
"""
from email.mime import image
from PIL import Image, ImageTk
import cv2
from pickle import FRAME
import tkinter as tk
from turtle import left
# from PIL import ImageTk, Image

from matplotlib.pyplot import text

# Create an instance of Tkinter's Tk class. assign it to window variables.
window = tk.Tk()

# Create Title Label
window.title("Image Editor")
    
frame = tk.Frame(window)
frame.pack(side = tk.TOP)
path = "/Users/natsu/Documents/ProgrammingProject/py-img-editor/img/kawai.jpg"
img = ImageTk.PhotoImage(Image.open(path))

# Create an empty label.
imgLabel = tk.Label(window, image = None)

entryInput = tk.Entry(frame, width = 60, text="the absolute path of Img with suffix")


def loadIMG():
    # Declare path for the image inputs.
    path = entryInput.get()
    # path = "img/ani.jpg"
    
    
    # print(path)
    # print(type(path))
    # print(type(Image.open(path)))
    
    # type(img)
    
    #-------------
    load = Image.open("img/ani.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(self, image=render)
    img.image = render
    img.pack()
    #-------------
    
    
    # img = ImageTk.PhotoImage(Image.open(path))
    # pic._image_ref = img
 
   
    # ---- try call front empty label ----   
    # img = Image.open(path)
    # render = ImageTk.PhotoImage(img)
    
    # imgLabel.config(image = render)
    # imgLabel.pack(side = tk.TOP)
    # --------------------------------------

# Create a button for loading images.
loadImgButton = tk.Button(
    frame,
    text="Load Img",
    bg="white",
    fg="black",
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
