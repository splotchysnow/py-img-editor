from curses.ascii import isdigit
import tkinter as tk
from globals import window
from tkinter import messagebox



"""
To put the Toplevel popup on the center of current window, it is recommend to ues position_center() right after you implement top level
"""
def position_center(top_name, width, height):
    winx = window.winfo_x()
    winy = window.winfo_y()
    win_w = window.winfo_width()
    win_h = window.winfo_height()
    top_name.geometry("%dx%d+%d+%d" % (width, height, winx+(win_w-width)/2, winy+(win_h-height)/2-30))
    # I don't want top-up be right center, so I get it down by 30




"""
Start of pop_filling(), it it build for fillingColor.py
    
"""
def popup_filling():
    global top_filling
    top_filling = tk.Toplevel(window)
    top_filling.grab_set()
    position_center(top_name=top_filling, width=450, height=120)
    color_var = tk.StringVar(top_filling, value="250,200,200")
    top_color_change(color_var)
    entry_input = tk.Entry(top_filling, width = 9, font = ('bold',20), textvariable= color_var)
    tor_frame = tk.Frame(top_filling)
    tor_msg = tk.Label(tor_frame, font=('',10), text="Color Difference tolerance, 0 - 100, default is 10")
    global entry_tor
    entry_tor = tk.Entry(tor_frame, font=('',8), width = 3)
    tor_msg.pack(side=tk.LEFT)
    entry_tor.pack(side=tk.LEFT)
    button = tk.Button(
        top_filling,
        text="Choose This Color",
        bg='white',
        fg="black",
        command=submit_filling
    )
    msg = tk.Label(top_filling, font=('bold',20),text="Input the Color you wanna fill, with #,#,# in RGB", bg='white')
    msg.pack(side=tk.TOP)
    entry_input.pack(side=tk.TOP)
    tor_frame.pack(side=tk.TOP)
    button.pack(side=tk.TOP)
    color_var.trace('w', lambda *args:top_color_change(color_var))

def top_color_change(var):
    color_decode(var)
    try:
        top_filling.config(bg = to_hex())
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
        top_filling.destroy()
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
Start of pop_drawing(), it is build for linCirRec_draw.py
"""

def popup_drawing():
    global top_choosing_mode
    top_choosing_mode = tk.Toplevel(window)
    position_center(top_choosing_mode, 300, 90)
    top_choosing_mode.grab_set()
    global tem_frame, mode_num
    tem_frame = tk.Frame(top_choosing_mode)
    mode_num = tk.IntVar(top_choosing_mode)
        
    lin_button = tk.Button(
        tem_frame,
        text="Drawing Line",
        width="12",
        bg='white',
        fg="black",
        command=lambda:draw_mode(1)
    )
    oval_button = tk.Button(
        tem_frame,
        text="Drawing Oval",
        width="12",
        bg='white',
        fg="black",
        command=lambda:draw_mode(2)
    )
    rect_button = tk.Button(
        tem_frame,
        text="Drawing Rectangle",
        width="12",
        bg='white',
        fg="black",
        command=lambda:draw_mode(3)
    )
    lin_button.pack(side=tk.TOP)
    oval_button.pack(side=tk.TOP)
    rect_button.pack(side=tk.TOP)
    tem_frame.pack()
    top_choosing_mode.wait_variable(mode_num)
    return mode_

def draw_mode(num):
    mode_num.set(num)
    tem_frame.destroy()
    canvas_for_example()

def canvas_for_example():
    top_choosing_mode.geometry("240x240")
    # mode is which shape we choose, shape is the object we will create later
    global mode_, color, thick, shape
    mode_ = mode_num.get()
    color = (0,0,0)
    thick = 1
    # make inner variables here
    global save_var, draw_color_var, draw_thick_var
    save_var = tk.IntVar(top_choosing_mode, value=0)
    draw_color_var = tk.StringVar(top_choosing_mode, value="0,0,0")
    draw_thick_var = tk.StringVar(top_choosing_mode,value=str(thick))
    
    # adding widges into top here
    global tem_canvas
    tem_canvas = tk.Canvas(top_choosing_mode, height=170)
    frame_two_enties = tk.Frame(top_choosing_mode)
    
    save_color_thick = tk.Button(
        top_choosing_mode,
        text="That's My Color & Thinkness",
        bg='white',
        fg='black',
        command=exit_top
    )

    if(mode_ == 1):
        shape = tem_canvas.create_line(30,50,210,50,fill=to_hex(),width=thick)
    elif(mode_ == 2):
        shape = tem_canvas.create_oval(20,20,220,150,outline=to_hex(),width=thick)
    else:
        shape = tem_canvas.create_rectangle(50,50,190,120,outline=to_hex(),width=thick)
        
    #pack things into frame here
    color_label = tk.Label(frame_two_enties,text="color:")
    color_entry = tk.Entry(frame_two_enties,width=5,textvariable=draw_color_var)
    thick_label = tk.Label(frame_two_enties,text="thick:")
    thick_entry = tk.Entry(frame_two_enties,width=2,textvariable=draw_thick_var)
    color_label.pack(side=tk.LEFT)
    color_entry.pack(side=tk.LEFT)
    thick_label.pack(side=tk.LEFT)
    thick_entry.pack(side=tk.LEFT)
    
    
    tem_canvas.pack(side=tk.TOP, expand=tk.YES)
    frame_two_enties.pack(side=tk.TOP)
    save_color_thick.pack(side=tk.TOP)
    
    #to monitor changes, think or color
    draw_color_var.trace('w', lambda *args:draw_color_change(draw_color_var))
    draw_thick_var.trace('w', lambda *args:draw_thick_change(draw_thick_var))
    top_choosing_mode.wait_variable(save_var)
    
def draw_color_change(var):
    color_decode(var)
    try:
        if mode_ == 1:
            tem_canvas.itemconfig(shape,fill=to_hex())
        else:    
            tem_canvas.itemconfig(shape,outline=to_hex())
    except:
        pass
    
def draw_thick_change(var):
    global thick
    thick = var.get()
    try: 
        tem_canvas.itemconfig(shape,width=thick)
    except:
        pass
    
def exit_top():
    if color_valid():
        if thick_valid():
            save_var.set(1)
            global color
            R, G, B = color
            color = (B,G,R)
            top_choosing_mode.destroy()
        else:
            messagebox.showwarning(title='Invalid thinkness', message='thick should be number and larger than 0')
    else:
        messagebox.showwarning(title='Invalid Color', message='color should be as form as #,#,#, with each # between 0 and 225')

def thick_valid():
    return thick.isnumeric() and int(thick) > 0
    
"""
End of pop_up_drawing here
"""


    
    
    
    
    
    