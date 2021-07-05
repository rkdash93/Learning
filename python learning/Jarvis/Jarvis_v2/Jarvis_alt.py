import speech_recognition as sr
import pyttsx3
import wikipedia
import random
import os,signal
import subprocess
import psutil
import webbrowser
import requests,json,urllib,re
from pyttsx3.drivers import sapi5
from playsound import playsound
from datetime import datetime
import time
import vlc
import pafy



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
        temperature = round(main['temp']) - 273
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']
        speak('Here is the weather details for ' + CITY)
        weather_data = f"\n{CITY:-^30}\nTemperature: {temperature} degrees celsius\nHumidity: {humidity}\nPressure: {pressure}\nWeather Report: {report[0]['description']}"
        #time.sleep(2)
        return weather_data
    else:
        # showing the error message
        error_msg='Error in the HTTP request'
        return error_msg

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
                elif 'what is the weather in' in cmd:
                    cmd = cmd.replace('what is the weather in ', '')
                    weather_data = weather(cmd)
                    print(weather_data)
                    speak (weather_data)
                                        
                elif 'play music' in cmd:
                    speak('Playing music....')
                    print('Playing music....')
                    music_files = os.listdir('.\\audio')
                    audio = '.\\audio\\' + str(random.choice(music_files))
                    # creating a vlc instance
                    vlc_instance = vlc.Instance()
                    # creating a media player
                    player = vlc_instance.media_player_new()
                    # creating a media
                    media = vlc_instance.media_new(audio)
                    # setting media to the player
                    player.set_media(media)
                    # play the video 
                    player.play()
                    # wait time
                    time.sleep(5)                    
                elif 'pause music' in cmd:
                    speak('Pausing music....')
                    print('Pausing music....')
                    player.pause()                    
                elif 'resume music' in cmd:
                    speak('playing music....')
                    print('playing music....')
                    player.play()                     
                    
                elif 'stop music' in cmd:
                    speak('Stopping music....')
                    print('Stopping music....')
                    player.stop()
                elif 'play' in cmd:
                    cmd=cmd.replace('play ','')
                    song='Playing ' + cmd
                    speak(song)
                    print(song + '....')                    
                    cmd=cmd.replace(' ','+')
                    youtube = urllib.request.urlopen('https://www.youtube.com/results?search_query='+cmd)
                    #print(youtube.read().decode())
                    video_ids = re.findall(r'watch\?v=(\S{11})',youtube.read().decode())
                    print(video_ids)
                    url = "https://www.youtube.com/watch?v=" + str(video_ids[0])
                    print(url)
                    video = pafy.new(url)
                    best = video.getbestaudio()
                    media = vlc.MediaPlayer(best.url)
                    media.play()
                    time.sleep(7)
                elif 'pause' in cmd:
                    speak('Pausing music....')
                    print('Pausing music....')
                    media.pause()                    
                elif 'resume' in cmd:
                    speak('playing music....')
                    print('playing music....')
                    media.play()                     
                    
                elif 'stop' in cmd:
                    speak('Stopping music....')
                    print('Stopping music....')
                    media.stop()                                                                 
                elif 'tell me about' in cmd:
                    speak('Searching wikipedia')
                    print('Searching wikipedia....')
                    cmd = cmd.replace('tell me about ', '')
                    try:
                        results = wikipedia.summary(cmd,sentences=2)
                        print(results)
                        speak(results)
                    except Exception as e:
                        print('No results found')
                        speak('No results found')
                elif 'agenda for today' in cmd:
                    if os.stat("agenda.txt").st_size == 0:
                        print('You have no agenda for today')
                        speak('You have no agenda for today')
                    else:                                        
                        f = open("agenda.txt", "r")
                        agenda = f.read()
                        f.close()
                        print('You have following agenda for today')
                        speak('You have following agenda for today')                        
                        print(agenda)
                        speak(agenda)
                elif 'news' in cmd:
                    url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=ad16f11716144daa93f97bf92e78c550')
                    response = requests.get(url).json()['articles']
                    news_article = []
                    print('Here are top 5 headlines for today')
                    speak('Here are top 5 headlines for today')
                    for i in response:
                        news_article.append(i['title'])
                    for j in range(5):
                        print(j+1,news_article[j])
                        speak(news_article[j])                                                
                elif 'what is' in cmd:
                    speak('Searching wikipedia')
                    print('Searching wikipedia....')
                    cmd = cmd.replace('what is ', '')
                    try:
                        results = wikipedia.summary(cmd,sentences=2)
                        print(results)
                        speak(results)
                    except Exception as e:
                        print('No results found')
                        speak('No results found')                        
                elif 'youtube' in cmd:
                    speak('Opening youtube')   
                    print('Opening YouTube.....')
                    webbrowser.open('www.youtube.com')
                elif 'google' in cmd:
                    speak('Opening google')   
                    print('Opening google.....')
                    webbrowser.open('www.google.com')
                elif 'search' in cmd:
                    cmd = cmd.replace('search ','')
                    speak('Searching in google')   
                    print('Searching in google.....')
                    webbrowser.open('https://www.google.com/search?q=' + str(cmd) )                    
                elif 'bye' in cmd:
                    break                         

