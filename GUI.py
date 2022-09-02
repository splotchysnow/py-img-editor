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
#path = "/Users/natsu/Documents/ProgrammingProject/py-img-editor/img/select.jpg"
#img = ImageTk.PhotoImage(Image.open(path))

# Create an empty label.
imgLabel = tk.Label(window)

entryInput = tk.Entry(frame, width = 60, text="the absolute path of Img with suffix")


def loadIMG():
    path = entryInput.get()
    img = ImageTk.PhotoImage(Image.open(path))
    imgLabel.config(image=img)
    imgLabel.pack()
    tk.update()
    
    #img = cv2.imread(path)
    #cv2.imshow("window",img)


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
