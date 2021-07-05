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
from env import *

#speech section

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('volume',1.0)
#engine.setProperty('rate',185)

r1=sr.Recognizer()


def speak(text):
    engine.say(text)
    engine.runAndWait()




def hello_jv():


    with sr.Microphone() as source:
        playsound('Speech On.wav')
        print('Listening...')
        #r1.adjust_for_ambient_noise(source)
        audio1=r1.listen(source)

    
    try:
            st=r1.recognize_google(audio1,language='en-in')
            print(f'{st}\n')

            if 'weather in ' in st:
                CITY = st.replace('what is the weather in','').strip()
                speak('checking weather for ' + CITY)
                print('checking weather for ' + CITY)
                weather(CITY)
            else:
                speak('I do not understand. Please use the type option')
                print('I do not understand. Please use the type option')
   

                
    except:
            speak('I do not understand. Please use the type option')
            print('exception')



def weather(CITY):

    # base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    # API key 
    API_KEY = "cb900a9371acdd246d7a78da15c7a143"
    # upadting the URL
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp'] - 273
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']
        speak('Here is the weather details for ' + CITY)
        print('Here is the weather details for ' + CITY)
        print(f"{CITY:-^30}")
        print(f"Temperature: {temperature} degrees celsius")
        print(f"Humidity: {humidity}")
        print(f"Pressure: {pressure}")
        print(f"Weather Report: {report[0]['description']}")
    else:
        # showing the error message
        print("Error in the HTTP request")

hello_jv()