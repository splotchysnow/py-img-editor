
from main_function_helper import *
def main():
    """
        Main function used for the whole flow of the GUI projects.
    """    
    # # Create an instance of Tkinter's Tk class. assign it to window variables.
    # window = globals.window
    
    # Create Title Label
    frame = tk.Frame(window)
    frame.pack(side = tk.TOP)

    # global canvas
    # canvas = globals.canvas

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
    operation_side()
    window.bind('<Escape>', quit)
    window.mainloop()
    
if __name__ == "__main__":
    main()