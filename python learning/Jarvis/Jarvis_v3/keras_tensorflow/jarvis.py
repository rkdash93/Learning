import vlc
import pafy
from time import sleep
from speak import speak,wake,task
from weather import *
from news_updates import news
from youtube_music import y_search

music_play = 0

if __name__ == "__main__":

    while True:
        tag = wake()
        if music_play == 1:            
            if player.is_playing() == 0:
                player.play()        
        if tag == 'wake':
            if music_play == 1:
                player.pause()            
            task_tag,task_resp,task_cmd = task()
            print(task_resp)
            speak(task_resp)
            if task_tag == 'weather':
                wather_report = weather(task_cmd)
                print(wather_report)
                speak(wather_report)
            elif task_tag == 'news':
                news()
            elif task_tag == 'play music':
                song,url = y_search(task_cmd)
                video = pafy.new(url)
                best = video.getbestaudio()
                player = vlc.MediaPlayer(best.url)
                player.audio_set_volume(50)
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
