import numpy as np
import os
import webbrowser
import json,requests
import random
import wikipedia
from api_keys import *
import re
import urllib,requests
from time import sleep,strftime
from datetime import datetime,date
from speak import *

# Agenda

def agenda_func(tsk):
    if tsk == 'write':
        print('What should I add?')
        speak('What should I add?')
        par1,par2,cmd_agenda = task('agenda')
        agenda_line = cmd_agenda
        cmd_agenda = 'Should I add ' + cmd_agenda.lower()
        print(cmd_agenda)
        speak(cmd_agenda)
        par1,par2,cmd_conf = task('agenda')
        if 'yes' in cmd_conf or 'yash' in cmd_conf.lower():
            f = open(r".\\data\\agenda.txt","a")
            f.writelines("\n"+agenda_line)
            f.close()
            print("Agenda added")
            speak("Agenda added")
        else:
            print("No agenda added")
            speak("No agenda added")            

    if tsk == 'read':
        f = open('.\\data\\agenda.txt')
        agenda = f.read()[10:]
        if len(agenda) > 0:
            print('You have following agenda for today')
            speak('You have following agenda for today')            
            print(agenda)
            speak(agenda)
        else:
            print("You don't have anything for today")
            speak("You don't have anything for today")
        f.close()         
          
# Reminder

def remind_func(tsk):
    if tsk == 'remind':
        print('What should I remind?')
        speak('What should I remind?')
        par1,par2,rem_task = task('reminder')
        print('What should be the time?')
        speak('What should be the time?')
        par1,par2,time_task = task('reminder')
        print('Remind you to ' + rem_task.lower() + ' at ' + time_task.lower() + '. Confirm?')
        speak('Remind you to ' + rem_task.lower() + ' at ' + time_task.lower() + '. Confirm?')
        par1,par2,conf_task = task('reminder')
        if 'yes' in conf_task.lower() or 'yash' in conf_task.lower():
            print('Reminder added')
            speak('Reminder added')
            time_task = datetime.strptime(time_task.replace('.',''),'%I:%M %p')
            return rem_task,time_task
        else:
            print('No reminder added')
            speak('No reminder added')
            time_task = datetime.strptime('12:00 AM','%I:%M %p')
            return rem_task,time_task

# launch application

path = np.array(["C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
                "C:\\Windows\\system32\\cmd.exe",
                "C:\\Program Files\\Git\\git-bash"])

def launch_app(app_cmd):
    if 'google' in app_cmd.lower():
        print('Opening google.....')
        speak('Opening google.....')
        webbrowser.open('www.google.com')
    elif 'youtube' in app_cmd.lower():
        print('Opening youtube. You are in a mood of watching videos')
        speak('Opening youtube. You are in a mood of watching videos')
        webbrowser.open('www.youtube.com')
    elif 'code' in app_cmd.lower():
        print('Opening visual studio code. It seems, we will be working on a new project')
        speak('Opening visual studio code. It seems, we will be working on a new project')
        os.startfile(path[0])
    elif 'command prompt' in app_cmd.lower():
        print('Opening command prompt.....')
        speak('Opening command prompt.....')
        os.startfile(path[1])
    elif 'git' in app_cmd.lower():
        print('Opening git-bash. It seems we are going to check-in the code')
        speak('Opening git-bash. It seems we are going to check-in the code')
        os.startfile(path[2])        
    else:
        print('I cannot do that')
        speak('I cannot do that')

# news updates

def news():
    url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey='+NEWS_API_KEY)
    response = requests.get(url).json()['articles']
    news_article = []
    for i in response:
        news_article.append(i['title'])
    for j in range(5):
        print(j+1,news_article[j])
        speak(news_article[j]) 

# paheli 

def paheli():
    p_list = ['Din may soye, raat may roye. Jitnaa roye utna khoye. Bolo kon hai ye', 
    'Ek thaal moti say bharaa, sir kay oopar awndhaa dharaa; Jaisay jaisay thaal phiray, moti ussay ek naa geeray',
    'Aisa likhiye sabd banaaye, phal, phool, aur mithai bun jaaye']
    sel_p = random.choice(p_list)
    print(sel_p)
    speak(sel_p)
    par1,par2,task_paheli = task('paheli')
    #task_paheli = input('Enter answer:')

    if sel_p == 'Din may soye, raat may roye. Jitnaa roye utna khoye. Bolo kon hai ye' and (task_paheli.lower() =='mombatti' or task_paheli =='candle'):
        speak('sahi jawaab')
        print('sahi jawaab')
    elif sel_p == 'Ek thaal moti say bharaa, sir kay oopar awndhaa dharaa; Jaisay jaisay thaal phiray, moti ussay ek naa geeray' and (task_paheli.lower() == 'aasman' or task_paheli == 'akash'):
        speak('sahi jawaab')
        print('sahi jawaab')
    elif sel_p == 'Aisa likhiye sabd banaaye, phal, phool, aur mithai bun jaaye' and task_paheli.lower() == 'gulab jamun':    
        speak('sahi jawaab')
        print('sahi jawaab')
    else:
        speak('galat jawaab')
        print('galat jawab')


# search

def search(task_cmd):
    if 'is' in task_cmd.lower():
        task_cmd = task_cmd.lower().rsplit("is ",1)[1]
    elif 'about' in task_cmd.lower():
        task_cmd = task_cmd.lower().rsplit("about ",1)[1]
    # print(task_cmd)
    try:
        results = wikipedia.summary(task_cmd,sentences=2)
        print(results)
        speak(results)
    except Exception as e:
        print('No results found')
        speak('No results found')           

# weather

def weather(task_cmd):
    if 'for' in task_cmd:
        CITY = task_cmd.lower().rsplit("for ",1)[1]
    elif 'in' in task_cmd:
        CITY = task_cmd.lower().rsplit("in ",1)[1]
    else:
        CITY = task_cmd.lower().rsplit(" ",1)[1]     

    # base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    # API key 
    API_KEY = WEATHER_API_KEY
    # upadting the URL
    URL = BASE_URL + "q=" + CITY + "&units=metric&appid=" + API_KEY
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = round(main['temp'])
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']
        #speak('Here are the weather details for' + CITY)        
        weather_data = f"\n{CITY:-^30}\nTemperature: {temperature} degrees celsius\nHumidity: {humidity}\nPressure: {pressure}\nWeather Report: {report[0]['description']}"
        #time.sleep(2)
        print(weather_data)
        speak(weather_data)
    else:
        # showing the error message
        error_msg='Error in the HTTP request'
        print(error_msg)
        speak(error_msg)

# music
def y_search(search,h_e_param):
    if h_e_param == 'e':
        search=search.replace('play ','')
    elif h_e_param == 'h':
        search=search.replace('sunao ','')                    
    search=search.replace(' ','+')
    #print(search)
    youtube = urllib.request.urlopen('https://www.youtube.com/results?search_query='+search)
    #print(youtube.read().decode())
    video_ids = re.findall(r'watch\?v=(\S{11})',youtube.read().decode())
    #print(video_ids)
    y_url = "https://www.youtube.com/watch?v=" + str(video_ids[0])
    return y_url