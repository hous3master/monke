import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

root = tk.Tk()
root.withdraw()  # Hide the main window

while True:
    x = random.randint(0, root.winfo_screenwidth())
    y = random.randint(0, root.winfo_screenheight())
    
    # Load the image
    image = Image.open("E:/u20211c795/monito.jpg")
    photo = ImageTk.PhotoImage(image)
    
    # Create a custom message box with an image
    custom_box = tk.Toplevel(root)
    custom_box.geometry("+%d+%d" % (x, y))  # Set the position of the custom message box
    custom_box.title("Custom Message Box")
    label = tk.Label(custom_box, text="Fuiste")
    label.pack()
    image_label = tk.Label(custom_box, image=photo)
    image_label.pack()
    custom_box.focus_set()
    custom_box.grab_set()
    custom_box.wait_window()