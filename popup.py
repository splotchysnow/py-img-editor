import tkinter as tk
import globals
from tkinter import messagebox


"""
Start of pop_filling()
    
"""
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
        bg='white',
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


"""
End of pop_filling here
"""






"""
Start of pop_drawing
"""

def popup_drawing():
    win = globals.window
    global top_choosing_mode
    top_choosing_mode = tk.Toplevel(win)
    top_choosing_mode.grab_set()
    top_choosing_mode.geometry("300x120")
    global mode_num
    mode_num = tk.IntVar(top_choosing_mode)
    lin_button = tk.Button(
        top_choosing_mode,
        text="Drawing Line",
        bg='white',
        fg="black",
        command=line_mode
    )
    circ_button = tk.Button(
        top_choosing_mode,
        text="Drawing Circle",
        bg='white',
        fg="black",
        command=circ_mode
    )
    rect_button = tk.Button(
        top_choosing_mode,
        text="Drawing Rectangle",
        bg='white',
        fg="black",
        command=rect_mode
    )
    lin_button.pack(side=tk.TOP)
    circ_button.pack(side=tk.TOP)
    rect_button.pack(side=tk.TOP)
    top_choosing_mode.wait_variable(mode_num)
    return mode_num.get()
    

def line_mode():
    mode_num.set(1)
    top_choosing_mode.destroy()

def circ_mode():
    mode_num.set(2)
    top_choosing_mode.destroy()
    
def rect_mode():
    mode_num.set(3)
    top_choosing_mode.destroy()
    
    
    
    