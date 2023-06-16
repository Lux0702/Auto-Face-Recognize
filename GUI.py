import tkinter as tk
from tkinter import ttk
import cv2 as cv
from PIL import Image, ImageTk
import subprocess
root=tk.Tk()
root.geometry("640x480")
cap = cv.VideoCapture(0)
frameWidth = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
frameHeight = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
print("Frame size: {}x{}".format(frameWidth,frameHeight))
cap.set(3,640)
cap.set(4,480)

imgBackground = cv.imread('./background.png')

def stop_capture(self):
        self.is_capturing = False
        self.vid.release()
while True:
    success, img = cap.read()

    imgBackground[162:162+480,55:55+640] = img
    
    cv.imshow("Face Attedance", imgBackground)
    
    
    key = cv.waitKey(1)
    if key == ord('q'):
        break
# cap.release()

