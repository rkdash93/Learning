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

#Male or Female voice set up
engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


path = "D:\\python learning\\audio"

r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

#Greet user
def hello_jv():
    with sr.Microphone() as source:
        playsound('Speech On.wav')
        print('Listening.....')
        r1.adjust_for_ambient_noise(source)
        audio1=r1.listen(source)

    
    try:
            st=r1.recognize_google(audio1,language='en-in')
            print(f'{st}\n')
            if 'Jarvis' in st:
                speak('Hello user! Please identify yourself?')
                print('Hello user! Please identify yourself?')
                ident_jv()
                
    except:
            speak('I do not understand')
            print('I do not understand')

def ident_jv():
    with sr.Microphone() as source:
        playsound('Speech On.wav')
        print('Listening.....')
        r2.adjust_for_ambient_noise(source)
        audio2=r2.listen(source)
    
    try:
            st1=r2.recognize_google(audio2,language='en-in')
            print(f'{st1}\n')
            if 'February' in st1:
                speak('Hello Pintu! How can I help you?')
                print('Hello Pintu! How can I help you?')
                with sr.Microphone() as source:
                    playsound('Speech On.wav')
                    print('Listening.....')
                    r3.adjust_for_ambient_noise(source)
                    audio=r3.listen(source)

                    try:
                        statement=r3.recognize_google(audio,language='en-in')
                        print(f'{statement}\n')
                        while True:
                            intr=take_cmd(statement)
                            if intr == 1:
                                break
                    except:
                        speak('I do not understand')
                        print('I do not understand')

            else:
                speak('Hello Guest! How can I help you?')
                print('Hello Guest! How can I help you?')
                with sr.Microphone() as source:
                    playsound('Speech On.wav')
                    print('Listening.....')
                    r3.adjust_for_ambient_noise(source)
                    audio=r3.listen(source)

                    try:
                        statement=r3.recognize_google(audio,language='en-in')
                        print(f'{statement}\n')
                        while True:
                            intr=take_cmd_guest(statement)
                            if intr == 1:
                                break
                    except:
                        speak('I do not understand')
                        print('I do not understand')                                              
    except:
            speak('Unauthorized user')
            print('Unauthorized user')
            exit()                

# taking user commands
def take_cmd(statement):
            if 'how are you doing' in statement:
                speak('I am doing great. Thanks!')
                print('I am doing great. Thanks!')

            elif 'Google' in statement:
                speak('Opening google')
                print('Opening google')
                webbrowser.open_new_tab('https://www.google.com')
                time.sleep(10)
                speak('Opened google')
                print('Opened google')

            elif 'YouTube' in statement:
                speak('Opening youtube')
                print('Opening youtube')
                webbrowser.open_new_tab('https://www.youtube.com')
                time.sleep(10)
                speak('Opened youtube')
                print('Opened youtube')
               
            elif 'Paint' in statement:
                speak('Opening paint')
                print('Opening paint')
                subprocess.run('C:\Windows\system32\mspaint.exe')

            elif 'search' in statement:
                speak('Searching')
                print('Searching')
                webbrowser.open_new_tab( 'https://www.google.com/search?q='+statement)
                time.sleep(15)
                speak('Found results for the search')
                print('Found results for the search')

            elif 'Kapil' in statement:
                speak('Searching')
                print('Searching')
                webbrowser.open_new_tab( 'https://www.youtube.com/search?q='+statement)
                time.sleep(15)
                speak('Found results for the search')
                print('Found results for the search')
            elif 'dialogue' in statement:
                files=os.listdir(path)
                d=random.choice(files)
                os.startfile(d)
#                playsound('Shahanshaah.mp3')
#                subprocess.run('C:\Program Files (x86)\Windows Media Player\wmplayer.exe')

            elif 'a joke' in statement:
                speak('Here is a joke that I know')
                print('Here is a joke that I know')
                speak('What do you call a talking dinosaur? A thesaurus')
                print('What do you call a talking dinosaur? A thesaurus')

            elif 'another joke' in statement:
                speak('Here is a joke that I know')
                print('Here is a joke that I know')
                speak('I taught a wolf to meditate. Now he is Aware Wolf.')
                print('I taught a wolf to meditate. Now he is Aware Wolf.')

            elif 'shutdown' in statement:
                speak('Shutting down')
                os.system('shutdown /s /t 1')

            elif 'bye' in statement:
                speak('Goodbye')
                print('Goodbye')
            return(1)
        



def take_cmd_guest(statement):
            if 'how are you doing' in statement:
                speak('I am doing great. Thanks!')
                print('I am doing great. Thanks!')
                return(0)
            elif 'dialogue' in statement:
                files=os.listdir(path)
                d=random.choice(files)
                os.startfile(d)
#                playsound('Shahanshaah.mp3')
#                subprocess.run('C:\Program Files (x86)\Windows Media Player\wmplayer.exe')
                return(0)
            elif 'a joke' in statement:
                speak('Here is a joke that I know')
                print('Here is a joke that I know')
                speak('What do you call a talking dinosaur? A thesaurus')
                print('What do you call a talking dinosaur? A thesaurus')
                return(0)
            elif 'another joke' in statement:
                speak('Here is a joke that I know')
                print('Here is a joke that I know')
                speak('I taught a wolf to meditate. Now he is Aware Wolf.')
                print('I taught a wolf to meditate. Now he is Aware Wolf.')
                return(0)
            elif 'bye' in statement:
                speak('Goodbye')
                print('Goodbye')
                return(1)
            else:
                speak('Your are not authorized to do that')
                print('Your are not authorized to do that')                
        


    

####UI section
def jv_ui():
    root = tk.Tk()
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


    label = tk.Label(root,image="")
    label.pack()

    update(count)
    root.mainloop()


if __name__=='__main__':
    p1 = Process(target = hello_jv)
    p1.start()    
    p2 = Process(target = jv_ui)
    p2.start()
    while True:
        if p1.is_alive() == False:
            p2.kill()
            break
 