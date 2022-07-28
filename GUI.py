"""
Create GUI with Tkinter for the software that we are designing.
"""

import tkinter as tk
from turtle import left

from matplotlib.pyplot import text

# Create an instance of Tkinter's Tk class. assign it to window variables.
window = tk.Tk()

# Create Title Label
titleLabel = tk.Label(text="Image Editor")


# Create a button for loading images.
loadImgButton = tk.Button(
    text="Load Img",
    width=10,
    height=1,
    bg="white",
    fg="black",
)

#Load the loading Button onto the Gui
titleLabel.pack(side=tk.LEFT)
loadImgButton.pack(side=tk.RIGHT)

# Create a label for the GUI that is related to the entry;
entryLabel = tk.Label(text="OutputFile Name")
#Create an entry so that when the user enters an string of text, it becomes the name of the output file.(AFTER EDIT:)
entryInput = tk.Entry(text="enter the output file name.")
#Create a button for collecting the entryInput name:
entryButton = tk.Button(text="save name")

entryLabel.pack(side = tk.BOTTOM)
entryButton.pack(side = tk.RIGHT)
entryInput.pack(side = tk.RIGHT)

# Run the tkinter event loop. Method Listens for events.
window.mainloop()