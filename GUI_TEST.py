import tkinter as tk
from tkinter import filedialog
import cv2
import PIL
from PIL import ImageTk,Image
import subprocess
from tkinter import *


def open_camera():
    subprocess.run(["python", 'get_face.py'], stdout=subprocess.PIPE, text=True)
def capture_image():
    subprocess.run(["python", 'Training.py'], stdout=subprocess.PIPE, text=True)
def check_in():
    subprocess.run(["python", 'predict.py'], stdout=subprocess.PIPE, text=True)

root = tk.Tk()

canvas = tk.Canvas(root, width=200, height=10)
canvas.pack()

text_label = tk.Label(root, text="Library UTE Check-in!")
text_label.place(relx=2, rely=2, anchor="n")
text_label.pack()
open_camera_button = tk.Button(root, text="Register", command=open_camera)
open_camera_button.pack()
capture_image_button = tk.Button(root, text="Training", command=capture_image)
capture_image_button.pack()
capture_image_button = tk.Button(root, text="Check-in", command=check_in)
capture_image_button.pack()





photo = None
cap = None

root.mainloop()