import speech_recognition as sr
import pyttsx3
from pyttsx3.drivers import sapi5
from playsound import playsound
from api_keys import *
from test_jarvis import *


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
            tag,resp = jarvis_response(cmd)
            #print(tag)
    except Exception as e:
        #print('Speak again')
        return "None"
    return tag

def task(param):
    speech_audio = '.\\sound\Speech On.wav'
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        #r.energy_threshold = 100
        r.pause_threshold = 1
        playsound(speech_audio)
        print('Listening....')
        try:        
            audio = r.listen(source,timeout=5,phrase_time_limit=4)
        except:
            pass
        try:
            cmd = r.recognize_google(audio,key=GOOGLE_API_KEY,language='en-in')
            print(cmd)
            if param == 'general':    
                tag,resp = jarvis_response(cmd)
                return tag,resp,cmd
            else:
                return "","",cmd    
        
        except sr.UnknownValueError:           
            speak('I do not understand')
            print('I do not understand')
            return "I do not understand","",""
        except sr.RequestError:
            print("Unable to connect to internet")
            speak("Unable to connect to internet")
            return "","",""
        except:
            print("I do not understand")
            speak("I do not understand")
            return "","",""                          


#speak("Badey badey desho may ayisi chotii chotii baathey ... hotii rehthii hai")        
         