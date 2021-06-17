import speech_recognition as sr
import pyttsx3
import wikipedia
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
 
                