from email import message
from operator import truediv
from pickle import FALSE, TRUE
import tkinter as tk
import globals
from tkinter import messagebox

color = (0,0,0)

def popup_filling():
    win = globals.window
    global top
    top = tk.Toplevel(win)
    top.grab_set()
    top.geometry("450x120")
    global color_var
    color_var = tk.StringVar(top, value="250,200,200")
    top_color_change()
    entry_input = tk.Entry(top, width = 9, font = ('bold',20), textvariable= color_var)
    tor_frame = tk.Frame(top)
    tor_msg = tk.Label(tor_frame, font=('',10), text="Color Difference tolerance, 0 - 100")
    global entry_tor
    entry_tor = tk.Entry(tor_frame, font=('',8), width = 3)
    tor_msg.pack(side=tk.LEFT)
    entry_tor.pack(side=tk.LEFT)
    button = tk.Button(
        top,
        text="Choose This Color",
        bg='blue',
        fg="black",
        command=submit_filling
    )
    msg = tk.Label(top, font=('bold',20),text="Input the Color you wanna fill, with #,#,# in RGB", bg='white')
    msg.pack(side=tk.TOP)
    entry_input.pack(side=tk.TOP)
    tor_frame.pack(side=tk.TOP)
    button.pack(side=tk.TOP)
    color_var.trace('w', lambda *args:top_color_change())

def top_color_change():
    color_decode()
    try:
        top.config(bg = to_hex())
    except:
        pass

def color_decode():
    global color
    R, B, G = color_var.get().split(",")
    color = (int(R),int(B),int(G))

def submit_filling():
        # cv2 use BRG, so we have to change format
    if color_valid():
        global color
        R, G, B = color
        global tol
        tol = entry_tor.get()
        color = (B,G,R)
        top.destroy()
    else:
        messagebox.showwarning(title='Invalid Color' ,message='should be #,#,# formate, and each # between 0 to 255')
    
def color_valid():
    for i in color:
        if i < 0 or i > 255:
            return False
    return True
    
def to_hex():
    r, g, b = color
    # background only accept hex format of color code
    return f'#{r:02x}{g:02x}{b:02x}'