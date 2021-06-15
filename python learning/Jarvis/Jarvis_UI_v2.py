import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import sys
import time
import subprocess
import random
import threading
import tkinter as tk
from playsound import playsound
from PIL import Image, GifImagePlugin
from multiprocessing import Process

engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

root = tk.Tk()
root.configure(bg='black')
file='Jarvis.gif'
#find number of frames
info = Image.open(file)
frames=info.n_frames

#create list of frames
im = [tk.PhotoImage(file=file,format=f'gif -index {i}') for i in range(frames)]

#function to iterate through list of frames
count = 0
def update(count):
    im2 = im[count]
    label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    root.after(100,lambda:update(count))

path = "D:\\python learning\\audio"

def loop_cmd(event):
    cmd = text.get("2.0","end-2c")
    
    if 'type' in cmd.lower():
        text.delete("1.0","2.0")
        speak('Hello user, please identify yourself')
        text.insert(tk.END,'Hello user, please identify yourself\n')
        text.delete("1.0","2.0")
        root.bind('<Return>',take_cmd)
    else:
        text.delete("1.0","2.0")
        speak('I do not understand')
        text.insert(tk.END,'I do not understand\n')
        quit()


        
def take_cmd(event):
        cmd = text.get("2.0","end-2c")

        if 'how are you doing' in cmd.lower():
            speak('I am doing good. Thanks!')
            text.insert(tk.END,'I am doing good. Thanks!\n')
            text.delete("1.0","3.0")

        elif 'a joke' in cmd.lower():
            speak('What do you call a talking dinosaur? A thesaurus')
            text.insert(tk.END,'What do you call a talking dinosaur? A thesaurus\n')
            text.delete("1.0","3.0")

        elif 'another joke' in cmd.lower():
            speak('I taught a wolf to meditate. Now he is Aware Wolf.')
            text.insert(tk.END,'I taught a wolf to meditate. Now he is Aware Wolf.\n')
            text.delete("1.0","3.0")

        elif 'google' in cmd.lower():
            speak('Opening google')
            text.insert(tk.END,'Opening google\n')
            text.delete("1.0","3.0")
            webbrowser.open_new_tab('https://www.google.com')
            time.sleep(10)
            speak('Opened google')
            text.insert(tk.END,'Opened google\n')
            text.delete("1.0","3.0")

        elif 'youtube' in cmd.lower():
            speak('Opening youtube')
            text.insert(tk.END,'Opening YouTube\n')
            text.delete("1.0","3.0")
            webbrowser.open_new_tab('https://www.youtube.com')
            time.sleep(10)
            speak('Opened youtube')
            text.insert(tk.END,'Opened YouTube\n')
            text.delete("1.0","3.0")

        elif 'paint' in cmd.lower():
            speak('Opening paint')
            subprocess.run('C:\Windows\system32\mspaint.exe')
            text.insert(tk.END,'Opened Paint\n')
            text.delete("1.0","3.0")

        elif 'search' in cmd.lower():
            speak('Searching')
            text.insert(tk.END,'Searching\n')
            text.delete("1.0","3.0")
            webbrowser.open_new_tab( 'https://www.google.com/search?q='+ cmd.lower())
            time.sleep(15)
            speak('Found results for the search')
            text.insert(tk.END,'Found results for the search\n')
            text.delete("1.0","3.0")

        elif 'kapil' in cmd.lower():
            speak('Searching')
            text.insert(tk.END,'Searching\n')
            text.delete("1.0","3.0")
            webbrowser.open_new_tab( 'https://www.youtube.com/search?q='+ cmd.lower())
            time.sleep(15)
            speak('Found results for the search')
            text.insert(tk.END,'Found results for the search\n')
            text.delete("1.0","3.0")
            
        
        elif 'who are you' in cmd.lower():            
            speak('I am Jarvis, your voice assistant')
            text.insert(tk.END,'I am Jarvis, your voice assistant\n')
            text.delete("1.0","3.0")

        elif 'bye' in cmd.lower():
            speak('Goodbye!')
            text.insert(tk.END,'Goodbye!\n')
            quit()
        elif 'shutdown' in cmd.lower():
            speak('Shutting down')
            os.system('shutdown /s /t 1')                   
        else:
            cmd = 'Hello ' + str(cmd) + ', how can I help you?\n'
            speak(cmd)
            text.insert(tk.END,cmd)
            text.delete("1.0","3.0")
            

    

def speak(text):
    engine.say(text)
    engine.runAndWait()


root.bind('<Return>',loop_cmd)


label = tk.Label(root,image="",borderwidth=0)
label.pack()

text = tk.Text(root, height = 5, width = 100)
#text.insert(tk.END,'Hello user, please identify yourself\n')
text.insert(tk.END,'Hello user, would you like to speak or type\n')
text.pack()

r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()


update(count)
#speak('Hello user, please identify yourself')
speak('Hello user, would you like to speak or type')


root.mainloop()
#hello_jv()




#anim(count)
