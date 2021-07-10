from speak import *
print("Jarvis is getting initialized. Please wait...........")
speak("Jarvis is getting initialized. Please wait...........")

import vlc
import pafy
import wikipedia
import os,sys
from time import sleep
from weather import *
from news_updates import news
from youtube_music import y_search
from datetime import datetime
from paheli import paheli
from agenda import remind_func,agenda_func
from launch_application import launch_app
from daily_task import daily_task


# initialize music,date,time variables
music_play = 0
today_date = datetime.now().strftime("%A,%d-%B-%Y")
input_time = datetime.strptime('12:00 AM','%I:%M %p')

# Reset agenda file everyday
agenda_today = datetime.now().strftime("%d-%m-%Y")
agenda_today = datetime.strptime(agenda_today,"%d-%m-%Y")
is_today = 1
f = open('.\\data\\agenda.txt','r')
agenda = f.readlines()[0:1]
for line in agenda:
    line = datetime.strptime(line.strip(),"%d-%m-%Y")
    if agenda_today > line:
        is_today = 0     
f.close()
if is_today == 0:
    f = open(r".\\data\\agenda.txt","w")
    f.writelines(agenda_today.strftime('%d-%m-%Y'))
    f.close()
daily_task()
# main execution    
if __name__ == "__main__":
    print("Jarvis is online and ready")
    speak("Jarvis is online and ready")
    while True:
        tag = wake()
        # continue playing music if already playing
        if music_play == 1:            
            if player.is_playing() == 0:
                player.play()
        # ring the alarm        
        if input_time.hour == datetime.now().hour:
            if input_time.minute == datetime.now().minute:
                rem_task = 'You have ' + remind_tsk + ' now'
                print(rem_task)
                speak(rem_task)
                playsound('.\\sound\\Alarm.wav')
                sleep (3)                         
        if tag == 'wake':
            # pause music when speaking the wake word
            if music_play == 1:
                player.pause()
            # task command for jarvis                
            task_tag,task_resp,task_cmd = task('general')
            print(task_resp)
            speak(task_resp)
            if task_tag == 'weather':
                wather_report = weather(task_cmd)
                print(wather_report)
                speak(wather_report)
            elif task_tag == 'news':
                news()
            elif task_tag == 'play music':
                # speak(task_resp)
                # print(task_resp)                
                url = y_search(task_cmd,'e')                
                video = pafy.new(url)
                best = video.getbestaudio()
                player = vlc.MediaPlayer(best.url)
                player.audio_set_volume(70)
                player.play()
                music_play = 1
                sleep(5)
            elif task_tag == 'play music hindi':               
                url = y_search(task_cmd,'h')
                video = pafy.new(url)
                best = video.getbestaudio()
                player = vlc.MediaPlayer(best.url)
                player.audio_set_volume(70)
                player.play()
                music_play = 1
                sleep(5)                
            elif task_tag == 'pause music':
                while player.is_playing() == 1:
                    player.pause()
                music_play = 0                     
            elif task_tag == 'resume music':
                player.play()                     
                music_play = 1
            elif task_tag == 'stop music':
                player.stop()
                music_play = 0
            elif task_tag == 'time':
                time_now = datetime.now().strftime("%I:%M %p")                
                print(time_now)
                speak(time_now)
            elif task_tag == 'today':
                print(today_date)
                speak(today_date)
            elif task_tag == 'paheli':
                paheli()
            elif task_tag == 'alarm':
                remind_tsk,input_time = remind_func('remind')
            elif task_tag == 'agenda':
                agenda_func('read')
            elif task_tag == 'add agenda':
                agenda_func('write')
            elif task_tag == 'application':
                launch_app(task_cmd)                                                
            elif task_tag == 'self train':
                os.startfile('train_jarvis.exe')
                sys.exit()
            elif task_tag == 'search':
                task_cmd = task_cmd.replace('tell me about ', '')
                try:
                    results = wikipedia.summary(task_cmd,sentences=2)
                    print(results)
                    speak(results)
                except Exception as e:
                    print('No results found')
                    speak('No results found')
            else:
                pass                                            


                                                                              
