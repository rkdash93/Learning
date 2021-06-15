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
import configparser

#speech section

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('volume',1.0)
#engine.setProperty('rate',185)

r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()


#fetch root user details from env file
config = configparser.ConfigParser()
config.read('Jarvis.env')
root_user=config.get('data','root_user')
#root_user=root_user.strip('\"')
passphrase=config.get('data','passphrase')
#passphrase=passphrase.strip('\"')
print(root_user)
print(passphrase)

#UI section

root = tk.Tk()
root.title('J.A.R.V.I.S')
root.configure(bg='#000606')
root.geometry('800x565')

battery = psutil.sensors_battery()
plugged = 'Plugged In' if battery[2] == True else 'Not Plugged In'

now=datetime.now()
curr_time = now.strftime('%I:%M %p')
curr_day=now.strftime('%A')

#find number of frames
file='Jarvis.gif'
info = Image.open(file)
frames=info.n_frames

#create list of frames
im = [tk.PhotoImage(file=file,format=f'gif -index {i}') for i in range(frames)]

#Image label
label = tk.Label(root,image="",bd=0)


#time label
time_img=tk.PhotoImage(file='jarvis_time1.png')

label3=tk.Label(root,image=time_img,borderwidth=0)

time_label=tk.Label(root,bg='#000606',text=str(curr_day) + ' : ' + str(curr_time) + '\nBattery : ' + str(battery[0]) + '%\n' + plugged ,font = ('Helvetica',14),fg='#00fffb')
#speak label
label2 = tk.Label(root,padx=5,height =7,width = 50,anchor='nw',bg='#001017',font = ('Arial',12),fg='#00fffb',bd = 3,relief = tk.RAISED)

#type text
text = tk.Text(root, padx=5, height = 7, width = 50,bg='#001017',font = ('Arial',12), fg='#00fffb',bd = 3,relief = tk.RAISED)
text.insert(tk.END,'Hello user, please identify yourself\n')

#buttons

mic_img=tk.PhotoImage(file='mic-button.png')
chat_img=tk.PhotoImage(file='chatbutton.png')

def b_type():
    label2.grid_forget()
    #t_button.grid_forget()
    text.grid(row=3,column=1)
    speak('Hello user, please identify yourself')
    root.bind('<Return>',type_ident_jv)

def b_speak():
    text.grid_forget()
    label2.grid(row=3,column=1)    
    hello_jv()

t_button = tk.Button(root,padx=10,image=chat_img,text = 'Type',font = ('Helvetica',12),fg='#ffffff',bd=1,bg = '#6e6a73', command = b_type)
s_button = tk.Button(root,padx=10,image=mic_img,text = 'speak',font = ('Helvetica',12),fg='#ffffff',bd=1,bg = '#6e6a73',command = b_speak)



#function for gif
count = 0
def update(count):
    im2 = im[count]
    label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    root.after(100,lambda:update(count))


#path = "D:\\python learning\\audio"
#type text function 

def type_ident_jv(event):
    cmd = text.get("2.0","end-2c")
    text.delete("1.0","3.0")
    global passphrase
    global root_user
    print (str(passphrase))
    print(cmd)    
    if cmd.lower() == passphrase.lower():
        cmd = 'Hello ' + root_user + '!, how can I help you?\n'
        speak(cmd)
        text.insert(tk.END,cmd)   
        root.bind('<Return>',type_cmd)
    else:
        type_cmd_guest(cmd)


def type_cmd(event):

        cmd = text.get("2.0","end-2c")
        path = "~\\audio"

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

        elif 'dialogue' in cmd.lower():
            files=os.listdir(path)
            d=random.choice(files)
            os.startfile(d)
            #subprocess.run('C:\Program Files (x86)\Windows Media Player\wmplayer.exe')            
        
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
        elif 'what is the weather in' in cmd.lower():
            CITY = cmd.replace('what is the weather in','').strip()
            speak('checking weather for ' + CITY)
            text.insert(tk.END,'checking weather for ' + CITY + '\n')
            weather(CITY,'type')            
        else:
            cmd = 'I do not understand\n'
            speak(cmd)
            text.insert(tk.END,cmd)
            text.delete("1.0","3.0")


def type_cmd_guest(cmd):

        cmd = text.get("2.0","end-2c")
        path = "~\\audio"

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


        elif 'dialogue' in cmd.lower():
            files=os.listdir(path)
            d=random.choice(files)
            os.startfile(d)
            #subprocess.run('C:\Program Files (x86)\Windows Media Player\wmplayer.exe')            
        
        elif 'who are you' in cmd.lower():            
            speak('I am Jarvis, your voice assistant')
            text.insert(tk.END,'I am Jarvis, your voice assistant\n')
            text.delete("1.0","3.0")

        elif 'bye' in cmd.lower():
            speak('Goodbye!')
            text.insert(tk.END,'Goodbye!\n')
            quit()

        else:
            cmd = 'Hello ' + str(cmd) + ', how can I help you?\n'
            speak(cmd)
            text.insert(tk.END,cmd)
            text.delete("1.0","3.0")            
                 


#Speak function

#greet user
def hello_jv():


    with sr.Microphone() as source:
        playsound('Speech On.wav')
        label2.configure(text='Listening...')
        label2.update()        
        #r1.adjust_for_ambient_noise(source)
        audio1=r1.listen(source)

    
    try:
            st=r1.recognize_google(audio1,language='en-in')
            #print(f'{st}\n')

            if 'Jarvis' in st:
                speak('Hello user! Please identify yourself?')
                label2.configure(text = 'Hello user! Please identify yourself?')
                label2.update()
                ident_jv()
            else:
                speak('I do not understand. Please use the type option')
                label2.configure(text = 'I do not understand. Please use the type option')
                label2.update()    

                
    except:
            pass
    
#Identify user
def ident_jv():
    with sr.Microphone() as source:
        playsound('Speech On.wav')
        label2.configure(text='Listening...')
        label2.update()
        #r2.adjust_for_ambient_noise(source)
        audio2=r2.listen(source)

    
    try:
            st1=r2.recognize_google(audio2,language='en-in')
            #print(f'{st1}\n')
            global passphrase
            global root_user
            if passphrase in st1:
                speak('Hello ' + root_user +'! How can I help you?')
                #print('Hello Pintu! How can I help you?')
                label2.configure(text='Hello ' + root_user +'! How can I help you?')
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
            pass                

# taking user commands
def take_cmd():
    with sr.Microphone() as source:
        playsound('Speech On.wav')
        label2.configure(text='Listening...')
        label2.update()
        #r3.adjust_for_ambient_noise(source)
        audio=r3.listen(source)

        try:
            statement=r3.recognize_google(audio,language='en-in')
            #print(f'{statement}\n')
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
            elif 'weather in' in statement:
                CITY = statement.replace('what is the weather in','').strip()
                speak('checking weather for ' + CITY)
                #print('checking weather for ' + CITY)
                label2.configure(text='checking weather for ' + CITY)
                label2.update()
                weather(CITY,'speak')
                return(0)                
        
        except:
            speak('I do not understand. Please use the type option')
            label2.configure(text='I do not understand.  Please use the type option')
            label2.update()
            return(1)


#weather details
def weather(CITY,flg):

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
        text.delete("1.0",tk.END)
        if flg == 'speak':
            label2.configure(text='Here is the weather details for ' + CITY)
            label2.update()
            label2.configure(text=f"\n{CITY:-^30}\nTemperature: {temperature} degrees celsius\nHumidity: {humidity}\nPressure: {pressure}\nWeather Report: {report[0]['description']}")
            label2.update()
        else:
            text.insert(tk.END,f"\n{CITY:-^30}\nTemperature: {temperature} degrees celsius\nHumidity: {humidity}\nPressure: {pressure}\nWeather Report: {report[0]['description']}\n")
        time.sleep(2)
    else:
        # showing the error message
        print("Error in the HTTP request")            

#guest user commands
def take_cmd_guest():
    with sr.Microphone() as source:
        playsound('Speech On.wav')
        label2.configure(text='Listening...')
        label2.update()
        #r3.adjust_for_ambient_noise(source)
        audio=r3.listen(source)

        try:
            statement=r3.recognize_google(audio,language='en-in')
            #print(f'{statement}\n')
            if 'how are you doing' in statement:
                speak('I am doing great. Thanks!')
                label2.configure(text='I am doing great. Thanks!')
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
            elif 'bye' in statement:
                speak('Goodbye')
                label2.configure(text='Goodbye')
                label2.update()
                return(1)
            else:
                speak('Your are not authorized to do that')
                label2.configure(text='Your are not authorized to do that')
                label2.update()                
        
        except:
            pass     



#function call

update(count)
label.grid(row=0,column=1)
time_label.grid(row=1,column=0,pady=0,sticky=tk.NW)
label3.grid(row=0,column=0)
t_button.grid(row=2,column=0,sticky=tk.NW)
s_button.grid(row=3,column=0,sticky=tk.NW,pady=10)

speak('Hello user, would you like to speak or type')
label2.configure(text='Hello user, would you like to speak or type')
label2.update()
label2.grid(row=3,column=1) 
root.mainloop()

