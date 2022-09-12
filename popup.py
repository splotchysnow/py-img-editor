import tkinter as tk
import globals

color = (0,0,0)

def popup_filling():
    win = globals.window
    top = tk.Toplevel(win)
    top.grab_set()
    top.geometry("400x100")
    entryInput = tk.Entry(top, width = 10)
    entryInput.insert(0, "250,200,200")
    button = tk.Button(
        top,
        text="Choose This Color",
        bg='white',
        fg="black",
        command=lambda:submit_filling(entryInput.get(), top)
    )
    msg = tk.Label(top, text="Input the Color you wanna fill, with #,#,# in RGB", bg='white')
    msg.pack(side=tk.TOP)
    entryInput.pack(side=tk.TOP)
    button.pack(side=tk.TOP)

def color_decode(input_color):
    global color
    B, G, R = input_color.split(",")
    color = (R,G,B)
    return color

def submit_filling(input_color, TOP):
    color_decode(input_color)
    TOP.destroy()
    
    