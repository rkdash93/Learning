import speech_recognition as sr
import pyttsx3
import wikipedia
import random
import os,signal
import subprocess
import psutil
from pyttsx3.drivers import sapi5
from playsound import playsound
from datetime import datetime



def speak(text):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[3].id)
    engine.setProperty('volume',1.0)        
    engine.say(text)
    engine.runAndWait()


def wake():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Passive listening....')
        #r.adjust_for_ambient_noise(source)
        #r.energy_threshold = 400
        #r.pause_threshold = 1
        audio = r.listen(source)    
    try:
            cmd = r.recognize_google(audio,key='AIzaSyDt-F9QddvrhHmigjv8nNJbFo_ArYl9k4c',language='en-in')
            print(cmd)
    except Exception as e:
        #print('Speak again')
        return "None"
    return cmd

def task():
    speech_audio = '.\\sound\Speech On.wav'
    r = sr.Recognizer()
    with sr.Microphone() as source:
        playsound(speech_audio)
        print('Listening....')
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)    
    try:
            cmd = r.recognize_google(audio,key='AIzaSyDt-F9QddvrhHmigjv8nNJbFo_ArYl9k4c',language='en-in')
            print(cmd)
    except Exception as e:
        #print('Speak again')
        return "None"
    return cmd  


def paheli():
    p_list = ['din may soye, raat may roye. Jitnaa roye utna khoye. Bolo kon hai ye', 'ek thaal moti say bharaa, sir kay oopar awndhaa dharaa; Jaisay jaisay thaal phiray, moti ussay ek naa geeray',
    'Aisa likhiye sabd banaaye, phal phool aur mithai ban jaaye']
    sel_p = random.choice(p_list)
    print(sel_p)
    speak(sel_p)
    speech_audio = '.\\sound\Speech On.wav'
    r = sr.Recognizer()
    with sr.Microphone() as source:
        playsound(speech_audio)
        print('Listening....')
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            cmd = r.recognize_google(audio,key='AIzaSyDt-F9QddvrhHmigjv8nNJbFo_ArYl9k4c',language='en-in')
            print(cmd)
        except Exception as e:
        #print('Speak again')
            return 'None','None'
         
    return sel_p,cmd
if __name__ == "__main__":        
    while True:
        greet = wake()
        if 'bhai Jarvis' in greet:
            speak('Hello user! aapki kyaa sewaa kar sakta hoo?')
            print('Hello user! aapki kya sewa kar sakta hun?')
            while True:
                cmd = task().lower()
                if 'tum kaun ho' in cmd:
                    speak('Mai Jarvis hoo, aapka voice assistant')
                    print('Main Jarvis hun, aapka voice assistant')
                elif 'kaise ho' in cmd:
                    speak('bahut badhiya')
                    print('Bahut badhiya')
                elif 'gana sunao' in cmd:
                    speak('abhih soonaatah hoo....')
                    print('abhi sunata hun....')
                    music_files = os.listdir('.\\audio')
                    audio = random.choice(music_files)
                    #os.startfile(f'.\\audio\\{audio}')
                    shell_process = subprocess.Popen(f'.\\audio\\{audio}',shell=True)
                    print(shell_process.pid)
                elif 'paheli poochho' in cmd:                    
                    speak('Paheli samjhoh aur jawaab doh')
                    print('Paheli samjho aur jawab do')    
                    sel_p,cmd=paheli()
                    print(sel_p)
                    print(cmd)
                    if sel_p == 'din may soye, raat may roye. Jitnaa roye utna khoye. Bolo kon hai ye' and (cmd =='mombatti' or cmd =='candle'):
                        speak('sahi jawaab')
                        print('sahi jawaab')
                    elif sel_p == 'ek thaal moti say bharaa, sir kay oopar awndhaa dharaa; Jaisay jaisay thaal phiray, moti ussay ek naa geeray' and cmd == 'aasman' or cmd == 'akash':
                        speak('sahi jawaab')
                        print('sahi jawaab')
                    elif sel_p == 'Aisa likhiye sabd banaaye, phal phool aur mithai ban jaaye' and cmd == 'gulab jamun':    
                        speak('sahi jawaab')
                        print('sahi jawaab')
                    else:
                        speak('galat jawaab')
                        print('galat jawab')                  
                    #print(p)                    

                elif 'bye' in cmd:
                    break              
        elif 'Jarvis' in greet:
            speak('Hello user! How can I help you?')
            print('Hello user! How can I help you?')
            while True:
                cmd = task().lower()
                if 'who are you' in cmd:
                    speak('I am Jarvis, your voice assistant')
                    print('I am Jarvis, your voice assistant')
                elif 'how are you doing' in cmd:
                    speak('I am doing good. Thanks!')
                    print('I am doing good. Thanks!')
                elif 'play music' in cmd:
                    speak('Playing music....')
                    print('Playing music....')
                    music_files = os.listdir('.\\audio')
                    audio = random.choice(music_files)
                    #os.startfile(f'.\\audio\\{audio}')
                    shell_process = subprocess.Popen([f'.\\audio\\{audio}'],shell=True)
                    parent = psutil.Process(shell_process.pid)
                    print(parent.pid)
                    #while(parent.children() == []):
                        #continue
                    children = parent.children(recursive=True)                    
                    #children = parent.children(recursive=True)
                    print(children)
                    #child_pid = children[0].pid
                    #print(child_pid)
                    
                elif 'stop music' in cmd:
                    speak('Stopping music....')
                    print('Stopping music....')
                    #subprocess.check_output("Taskkill /PID %d /F" % shell_process.pid)
                    os.system("taskkill  /F /pid "+str(shell_process.pid))                    
                elif 'tell me about' in cmd:
                    speak('Searching wikipedia')
                    print('Searching wikipedia....')
                    cmd = cmd.replace('tell me about', '')
                    try:
                        results = wikipedia.summary(cmd,sentences=2)
                        print(results)
                        speak(results)
                    except Exception as e:
                        print('No results found')
                        speak('No results found')   
                                        
                elif 'bye' in cmd:
                    break                         

