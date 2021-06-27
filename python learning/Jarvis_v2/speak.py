import speech_recognition as sr
import pyttsx3
from pyttsx3.drivers import sapi5
from playsound import playsound
from api_keys import *

def speak(text):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[3].id)
    engine.setProperty('rate', 178)
    engine.setProperty('volume',1.0)        
    engine.say(text)
    engine.runAndWait()

def wake():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Passive listening....')
        #r.adjust_for_ambient_noise(source)
        r.energy_threshold = 400
        #r.pause_threshold = 1
        audio = r.listen(source,phrase_time_limit=2)    
    try:
            cmd = r.recognize_google(audio,key=GOOGLE_API_KEY,language='en-in')
            print(cmd)
    except Exception as e:
        #print('Speak again')
        return "None"
    return cmd

def task():
    speech_audio = '.\\sound\Speech On.wav'
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        #r.energy_threshold = 100
        r.pause_threshold = 1
        playsound(speech_audio)
        print('Listening....')        
        audio = r.listen(source,timeout=5, phrase_time_limit=5)    
        try:
            cmd = r.recognize_google(audio,key=GOOGLE_API_KEY,language='en-in')
            print(cmd)
            return cmd
        except Exception as e:
            speak('I do not understand')
            return "I do not understand"
         