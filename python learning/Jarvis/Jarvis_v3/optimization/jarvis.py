from speak import *
print("Jarvis is getting initialized. Please wait...........")
speak("Jarvis is getting initialized. Please wait...........")
from daily_task import *
import vlc
import pafy
import sys,warnings
warnings.filterwarnings('ignore')
from task import *



# initialize music,date,time variables
music_play = 0
today_date = datetime.now().strftime("%A,%d-%B-%Y")
input_time = datetime.strptime('12:00 AM','%I:%M %p')


# #temporary code
# input_time = datetime.strptime('04:45 AM','%I:%M %p')
# remind_tsk = 'to wake up'

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
                sleep (2)                         
        if tag == 'wake':
            # pause music when speaking the wake word
            if music_play == 1:
                player.pause()
            # task command for jarvis                
            task_tag,task_resp,task_cmd = task('general')
            print(task_resp)
            speak(task_resp)
            if task_tag[-1:] == ")":
                exec(task_tag)
            # evaluate simple math expression
            # elif task_tag == 'eval':
            #     evaluate = task_cmd.lower().replace(' x ', '*')
            #     evaluate = task_cmd.lower().replace(' / ', '/')
            #     evaluate = evaluate.rsplit(" ",1)[1]
                
            #     # print(evaluate)
            #     try:
            #         print(eval(evaluate))
            #         speak(eval(evaluate))
            #     except Exception as e:
            #         print('I cannot do that')
            #         speak('I cannot do that')
                                            
            else:
                pass                                            


                                                                              
