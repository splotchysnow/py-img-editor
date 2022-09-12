import tkinter as tk
import globals

color = (0,0,0)

def popup_filling():
    win = globals.window
    global top
    top = tk.Toplevel(win)
    top.grab_set()
    top.geometry("400x100")
    global color_var
    color_var = tk.StringVar(top, value="250,200,200")
    top_color_change()
    entryInput = tk.Entry(top, width = 10, textvariable= color_var)
    button = tk.Button(
        top,
        text="Choose This Color",
        bg='white',
        fg="black",
        command=submit_filling
    )
    msg = tk.Label(top, text="Input the Color you wanna fill, with #,#,# in RGB", bg='white')
    msg.pack(side=tk.TOP)
    entryInput.pack(side=tk.TOP)
    button.pack(side=tk.TOP)
    color_var.trace('w', lambda *args:top_color_change())

def top_color_change():
    color_decode()
    if color_valid():
        return top.config(bg = to_hex())
    else:
        return None

def color_decode():
    global color
    try:
        R, B, G = color_var.get().split(",")
        color = (int(R),int(B),int(G))
        print(color)
    except:
        pass

def submit_filling():
    color_decode()
    if color_valid():
        # cv2 use BRG, so we have to change format
        global color
        R, G, B = color
        color = (B,G,R)
        top.destroy()
    else:
        tk.messagebox.showwarning('invalid color')
    
def color_valid():
    for i in color:
        if i < 0 | i > 255:
            return False
    return True
    
def to_hex():
    r, g, b = color
    return f'#{r:02x}{g:02x}{b:02x}'