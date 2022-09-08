from ctypes.wintypes import RGB
from readline import insert_text
import tkinter as tk
from turtle import bgcolor
import globals

color = RGB(0,0,0)

def popup_filling():
    win = globals.window
    top = tk.Toplevel(win)
    top.grab_set()
    top.geometry("400x100")
    msg = tk.Label(top, text="Input the Color you wanna fill, with #,#,# in RGB")
    entryInput = tk.Entry(top, width = 10)
    entryInput.insert(0, "100,200,100")
    button = tk.Button(
        top,
        text="Choose This Color",
        bg= "white",
        fg="black",
        command=lambda:submit_filling(entryInput.get(), top)
    )
    msg.pack(side=tk.TOP)
    entryInput.pack(side=tk.TOP)
    button.pack(side=tk.TOP)
    
def submit_filling(input_color, TOP):
    global color
    R, G, B = input_color.split(",")
    color = RGB(int(R),int(G),int(B))
    TOP.destroy()
    
    