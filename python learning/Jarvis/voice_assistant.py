import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import time
import subprocess
import random
from playsound import playsound

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voices",voices[1].id)

path = "D:\\python learning"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    speak('Hello user! Please identify yourself?')
    take_cmd()
    take_cmd()


def take_cmd():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f'{statement}\n')
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
                time.sleep(10)
                speak('Found results for the search')
                print('Found results for the search')
            elif 'Kapil' in statement:
                speak('Searching')
                print('Searching')
                webbrowser.open_new_tab( 'https://www.youtube.com/search?q='+statement)
                time.sleep(10)
                speak('Found results for the search')
                print('Found results for the search')
            elif 'dialogue' in statement:
                files=os.listdir(path)
                d=random.choice(files)
                os.startfile(d)
#                playsound('Shahanshaah.mp3')
#                subprocess.run('C:\Program Files (x86)\Windows Media Player\wmplayer.exe')
            elif 'shutdown' in statement:
                speak('Shutting down')
                subprocess.call(["shutdown"],"/l")
            else:
               speak('Hello '+ statement)
               print('Hello '+ statement)


           
        
        except:
            speak('I do not understand')
            print('I do not understand')

greet()
#take_cmd()