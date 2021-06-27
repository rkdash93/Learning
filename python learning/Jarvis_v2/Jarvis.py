
import wikipedia
import os
import webbrowser
import urllib,re
from datetime import datetime,date
from speak import *
from weather import *
from paheli import *
from agenda import *
import vlc
import pafy


music_play = 0
input_time = '12:00 AM'
input_time = datetime.strptime(input_time,'%I:%M %p') 


if __name__ == "__main__":
    #Reset agenda file everyday
    today = strftime("%d-%m-%Y")
    is_today = 1
    f = open('agenda.txt','r')
    agenda = f.readlines()[0:1]
    for line in agenda:
        if today > line.rstrip():
            is_today = 0       
    f.close()
    if is_today == 0:
        f = open(r"agenda.txt","w")
        f.writelines(today)
        f.close()
    
    print('Online and ready')
    speak('Online and ready')
    #Listen to user       
    while True:
        greet=wake()
        if music_play == 1:            
            if player.is_playing() == 0:
                player.play()
        if input_time.hour == datetime.now().hour:
            if input_time.minute == datetime.now().minute:
                rem_task = 'You have to ' + remind_tsk + ' now'
                print(rem_task)
                speak(rem_task)
                playsound('.\\sound\\Alarm.wav')
                sleep (3)                       
                     
        if 'jarvis' in greet.lower() or 'jarjis' in greet.lower() or 'javed' in greet.lower() or 'charges' in greet.lower() or 'service' in greet.lower():
            try:
                if music_play == 1:
                    player.pause()
                cmd = task().lower()
                if 'who are you' in cmd:
                    speak('I am Jarvis, your voice assistant')
                    print('I am Jarvis, your voice assistant')
                elif 'time now' in cmd or 'time' in cmd:
                    now_time = datetime.now().strfitme('%I:%M %p')
                    now_time = "time is " + now_time
                    print(now_time)
                    speak(now_time)
                elif 'date' in cmd:
                    date = datetime.now().strftime("%A %d-%B-%Y")
                    date = "today is " + date
                    print(date)
                    speak(date)                                         
                elif 'how are you doing' in cmd:
                    speak('I am doing good. Thanks!')
                    print('I am doing good. Thanks!')
                elif 'what is the weather in' in cmd:
                    cmd = cmd.replace('what is the weather in ', '')
                    weather_data = weather(cmd)
                    print(weather_data)
                    speak (weather_data)
                                        
                elif 'play my music' in cmd:
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
                    player.audio_set_volume(50)
                    # play the video 
                    player.play()
                    music_play = 1
                    # wait time
                    sleep(1)       


                elif 'play' in cmd:
                    cmd=cmd.replace('play ','')
                    song='Playing ' + cmd
                    speak(song)
                    print(song + '....')                    
                    cmd=cmd.replace(' ','+')
                    youtube = urllib.request.urlopen('https://www.youtube.com/results?search_query='+cmd)
                    #print(youtube.read().decode())
                    video_ids = re.findall(r'watch\?v=(\S{11})',youtube.read().decode())
                    #print(video_ids)
                    url = "https://www.youtube.com/watch?v=" + str(video_ids[0])
                    #print(url)
                    video = pafy.new(url)
                    best = video.getbestaudio()
                    player = vlc.MediaPlayer(best.url)
                    player.audio_set_volume(50)
                    player.play()
                    music_play = 1
                    sleep(7)                           
                elif 'pause' in cmd:
                    speak('Pausing music....')
                    print('Pausing music....')
                    while player.is_playing() == 1:
                        player.pause()
                    music_play = 0                     
                elif 'resume' in cmd:
                    speak('playing music....')
                    print('playing music....')
                    player.play()                     
                    music_play = 1
                elif 'stop' in cmd:
                    speak('Stopping music....')
                    print('Stopping music....')
                    player.stop()
                    music_play = 0                                                               
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
                elif 'add agenda' in cmd:
                    a_ret = agenda_func('write')                        
                elif 'agenda' in cmd:
                    a_ret = agenda_func('read')
                elif 'news' in cmd:
                    url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey='+NEWS_API_KEY)
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
                elif 'tum kaun ho' in cmd:
                    speak('Mai Jarvis hoo, aapka voice assistant')
                    print('Main Jarvis hun, aapka voice assistant')
                elif 'kaise ho' in cmd:
                    speak('bahut badhiya')
                    print('Bahut badhiya')
                elif 'kya chal raha hai' in cmd:
                    res_list = ['Fog chal raha hai',
                    'Bus chill kar raha hoo',
                    'reading news, to get news updates please say Jarvis what is the news for today']
                    res = random.choice(res_list)
                    speak(res)
                    print(res)                    
                elif 'gana sunao' in cmd:
                    speak('abhih soonaatah hoo....')
                    print('abhi sunata hun....')
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
                    player.audio_set_volume(50)
                    # play the video 
                    player.play()
                    music_play = 1
                    # wait time
                    sleep(1)
                elif 'paheli poochho' in cmd or 'ek paheli pucho' in cmd:                    
                    speak('Paheli samjhoh aur jawaab doh')
                    print('Paheli samjho aur jawab do')    
                    paheli()

                elif 'reminder' in cmd:
                    remind_tsk,input_time = remind_func('remind')
                elif 'bye' in cmd:
                    break
            except:
                pass                        
