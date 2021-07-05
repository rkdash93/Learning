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

#type text function    
def type_cmd(event):
        
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
                 
#Speak function

def speak_jv():
    while True:
        label2.pack()
        with sr.Microphone() as source:
            playsound('Speech On.wav')
            r1.adjust_for_ambient_noise(source)
            audio1=r1.listen(source)

        try:
            st=r1.recognize_google(audio1,language='en-in')
            print(f'{st}\n')
            if 'a joke' in st.lower():
                speak('What do you call a talking dinosaur? A thesaurus')
                label2.configure(text = 'What do you call a talking dinosaur? A thesaurus')
                label.update()
            elif 'who are you' in st.lower():
                speak('I am Jarvis, your voice assistant')
                label2.configure(text = 'I am Jarvis, your voice assistant')
                label.update()
            elif 'bye'  in st.lower():
                speak('Goodbye!')
                label2.configure(text = 'Goodbye!')
                label.update()
                break                                     
                
        except:
             speak('I do not understand')
             label2.configure(text = 'I do not understand')
             break

               

        

def hello_jv():


    with sr.Microphone() as source:
        playsound('Speech On.wav')
        label2.configure(text='Listening...')
        label2.update()        
        r1.adjust_for_ambient_noise(source)
        audio1=r1.listen(source)

    
    try:
            st=r1.recognize_google(audio1,language='en-in')
            print(f'{st}\n')

            if 'Jarvis' in st:
                speak('Hello user! Please identify yourself?')
                label2.configure(text = 'Hello user! Please identify yourself?')
                label2.update()
                ident_jv()

                
    except:
            speak('I do not understand')
            label2.configure(text = 'I do not understand')
            label2.update()
    

def ident_jv():
    with sr.Microphone() as source:
        playsound('Speech On.wav')
        label2.configure(text='Listening...')
        label2.update()
        r2.adjust_for_ambient_noise(source)
        audio2=r2.listen(source)

    
    try:
            st1=r2.recognize_google(audio2,language='en-in')
            print(f'{st1}\n')
            if 'February' in st1:
                speak('Hello Pintu! How can I help you?')
                #print('Hello Pintu! How can I help you?')
                label2.configure(text='Hello Pintu! How can I help you?')
                label2.update()
                while True:
                    intr=take_cmd()
                    if intr == 1:
                        break

            else:
                speak('Hello Guest! How can I help you?')
                #print('Hello Guest! How can I help you?')
                label2.configure(text='Hello Guest! How can I help you?')
                label2.update()
                while True:
                    intr=take_cmd_guest()
                    if intr == 1:
                        break                                             
    except:
            speak('I do not understand')
            #print('Unauthorized user')
            label2.configure(text='I do not understand')
            label2.update()            
            exit()                

# taking user commands
def take_cmd():
    with sr.Microphone() as source:
        playsound('Speech On.wav')
        label2.configure(text='Listening...')
        label2.update()
        r3.adjust_for_ambient_noise(source)
        audio=r3.listen(source)

        try:
            statement=r3.recognize_google(audio,language='en-in')
            print(f'{statement}\n')
            if 'how are you doing' in statement:
                speak('I am doing great. Thanks!')
                label2.configure(text='I am doing great. Thanks!')
                label2.update()
                return(0)
            elif 'Google' in statement:
                speak('Opening google')
                label2.configure(text='Opening google')
                label2.update()
                webbrowser.open_new_tab('https://www.google.com')
                time.sleep(10)
                speak('Opened google')
                label2.configure(text='Opened google')
                label2.update()
                return(0)
            elif 'YouTube' in statement:
                speak('Opening youtube')
                label2.configure(text='Opening youtube')
                label2.update()
                webbrowser.open_new_tab('https://www.youtube.com')
                time.sleep(10)
                label2.configure(text='Opened youtube')
                label2.update()
                return(0)                
            elif 'Paint' in statement:
                speak('Opening paint')
                label2.configure(text='Opening paint')
                label2.update()
                subprocess.run('C:\Windows\system32\mspaint.exe')
                return(0)
            elif 'search' in statement:
                speak('Searching')
                label2.configure(text='Searching')
                label2.update()
                webbrowser.open_new_tab( 'https://www.google.com/search?q='+statement)
                time.sleep(15)
                speak('Found results for the search')
                label2.configure(text='Found results for the search')
                label2.update()
                return(0)
            elif 'Kapil' in statement:
                speak('Searching')
                label2.configure(text='Searching')
                label2.update()
                webbrowser.open_new_tab( 'https://www.youtube.com/search?q='+statement)
                time.sleep(15)
                speak('Found results for the search')
                label2.configure(text='Found results for the search')
                label2.update()   
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
                label2.configure(text='Here is a joke that I know')
                label2.update()
                speak('What do you call a talking dinosaur? A thesaurus')
                label2.configure(text='What do you call a talking dinosaur? A thesaurus')
                label2.update()
                return(0)

            elif 'another joke' in statement:
                speak('Here is a joke that I know')
                label2.configure(text='Here is a joke that I remember')
                label2.update()
                speak('I taught a wolf to meditate. Now he is Aware Wolf.')
                label2.configure(text='I taught a wolf to meditate. Now he is Aware Wolf.')
                label2.update()
                return(0)

            elif 'who are you' in statement:
                speak('I am Jarvis, your voice assistant')
                label2.configure(text='I am Jarvis, your voice assistant')
                label2.update()
                return(0)

            elif 'shutdown' in statement:
                speak('Shutting down')
                os.system('shutdown /s /t 1')
                return(0)

            elif 'bye' in statement:
                speak('Goodbye')
                label2.configure(text='Goodbye')
                label2.update()
                return(1)
        
        except:
            speak('I do not understand')
            label2.configure(text='I do not understand')
            label2.update()


def take_cmd_guest():
    with sr.Microphone() as source:
        playsound('Speech On.wav')
        print('Listening.....')
        r3.adjust_for_ambient_noise(source)
        audio=r3.listen(source)

        try:
            statement=r3.recognize_google(audio,language='en-in')
            print(f'{statement}\n')
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
        
        except:
            speak('I do not understand')
            print('I do not understand')    

def speak(text):
    engine.say(text)
    engine.runAndWait()



def b_type():
    label2.pack_forget()
    text.pack()
    speak('Hello user, please identify yourself')
    root.bind('<Return>',type_cmd)

def b_speak():
    text.pack_forget()
    label2.pack()
    label2.update()
    hello_jv()


label = tk.Label(root,image="",borderwidth=0)
label.pack()

label2 = tk.Label(root,height =5,width = 100,anchor='nw',bg='#1f1f2e',fg='#ffffff')

text = tk.Text(root, height = 5, width = 100,bg='#1f1f2e',fg='#ffffff',relief=tk.GROOVE)
text.insert(tk.END,'Hello user, please identify yourself\n')

t_button = tk.Button(root, text = 'type',command = b_type)
s_button = tk.Button(root, text = 'speak',command = b_speak)

t_button.pack(side = tk.LEFT)
s_button.pack(side = tk.LEFT)

r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()


update(count)

speak('Hello user, would you like to speak or type')


root.mainloop()

