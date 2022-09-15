import tkinter as tk
from typing_extensions import IntVar
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
    color_var.trace('w', lambda *args:top_color_change(color_var))

def top_color_change():
    color_decode()
    try:
        top.config(bg = to_hex())
    except:
        pass

def color_decode(var):
    global color
    R, B, G = var.get().split(",")
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
    top_choosing_mode.geometry("300x90")
    frame = top_choosing_mode.frame()
    
    global mode_num
    mode_num = tk.IntVar(top_choosing_mode)
    
    def draw_mode(num):
        mode_num.set(num)
        frame.destroy()
        canvas_for_example()
        
    lin_button = tk.Button(
        frame,
        text="Drawing Line",
        width="12",
        bg='white',
        fg="black",
        command=lambda:draw_mode(1)
    )
    oval_button = tk.Button(
        frame,
        text="Drawing Oval",
        width="12",
        bg='white',
        fg="black",
        command=lambda:draw_mode(2)
    )
    rect_button = tk.Button(
        frame,
        text="Drawing Rectangle",
        width="12",
        bg='white',
        fg="black",
        command=lambda:draw_mode(3)
    )
    lin_button.pack(side=tk.TOP)
    oval_button.pack(side=tk.TOP)
    rect_button.pack(side=tk.TOP)
    top_choosing_mode.wait_variable(mode_num)
    return mode_num.get()

def canvas_for_example():
    top_choosing_mode.geometry("250x200")
    
    # make inner variables here
    global save_var, draw_color_var, draw_thick_var
    save_var = tk.IntVar(top_choosing_mode value=0)
    draw_color_var = tk.StringVar(top_choosing_mode, value="0,0,0")
    draw_thick_var = tk.IntVar(top_choosing_mode,value=1)
    
    # pack into top here
    tem_canvas = tk.Canvas(top_choosing_mode)
    frame_two_enties = tk.Frame(top_choosing_mode)
    
    save_color_think = tk.Button(
        top_choosing_mode,
        text="That's My Color & Thinkness",
        textvariable=save_var,
        bg='white',
        fg='black',
        command=exit_top
    )
    tem_canvas.pack(side=tk.TOP)
    frame_two_enties(side=tk.TOP)
    save_color_think(side=tk.TOP)
    
    #pack things into frame here
    color_label = tk.Label(frame_two_enties, text="color")
    color_entry = tk.Entry(frame_two_enties, textvariable=draw_color_var)
    thick_label = tk.Label(frame_two_enties, text="thick")
    thick_entry = tk.Entry(frame_two_enties, textvariable=draw_thick_var)
    color_label.pack(side=tk.LEFT)
    color_entry.pack(side=tk.LEFT)
    thick_label.pack(side=tk.LEFT)
    thick_entry.pack(side=tk.LEFT)
    
    #to monitor changes
    global color, thick
    color = (0,0,0)
    thick = 1
    draw_color_var.trace('w', lambda *args:draw_color_change())
    draw_thick_var.trace('w', lambda *args:draw_thick_change())

def draw(args):
    
    
    
    
    
    
    