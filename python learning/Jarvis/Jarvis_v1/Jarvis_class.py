import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser
import os
import sys
import time
import subprocess
import random
import tkinter as tk
from playsound import playsound
from PIL import Image, GifImagePlugin
from pyttsx3.drivers import sapi5
import psutil
import requests,json
import configparser


class jv_ui():
    root = tk.Tk()
    root.title('J.A.R.V.I.S')
    root.configure(bg='#000606')
    root.geometry('800x565')

    
    #label = tk.Label(root,text='Hello user')
    img_file='Jarvis.gif'

    #find number of frames
    info = Image.open(img_file)
    frames=info.n_frames

    #create list of frames
    im = [tk.PhotoImage(file=img_file,format=f'gif -index {i}') for i in range(frames)]

    count = 0
    def update(self,count):
        self.im2 = self.im[count]
        self.label.configure(image=im2)
        self.count += 1
        if self.count == frames:
            self.count = 0
            self.root.after(100,lambda:update(count))

    label = tk.Label(root,image="",borderwidth=0,bg='#000606')

    




    def __init__(self):
        self.update(0)
        self.label.pack()
        self.root.mainloop()

    

root = jv_ui()






