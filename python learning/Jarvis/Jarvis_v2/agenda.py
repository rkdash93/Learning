from time import sleep,strftime
from datetime import datetime,date
from speak import *

def agenda_func(tsk):
    if tsk == 'write':
        print('What should I add?')
        speak('What should I add?')
        cmd_agenda = task().lower()
        agenda_line = cmd_agenda
        cmd_agenda = 'Should I add ' + cmd_agenda
        print(cmd_agenda)
        speak(cmd_agenda)
        cmd_conf = task().lower()
        if cmd_conf == 'yes':
            f = open(r"agenda.txt","a")
            f.writelines("\n"+agenda_line)
            f.close()
            print("Agenda added")
            speak("Agenda added")
        else:
            print("No agenda added")
            speak("No agenda added")            

    if tsk == 'read':
        print('You have following agenda for today')
        speak('You have following agenda for today')
        f = open('agenda.txt')
        agenda = f.read()
        print(agenda)
        speak(agenda)
        f.close()

    return(1)    

def remind_func(tsk):
    if tsk == 'remind':
        print('What should I remind?')
        speak('What should I remind?')
        rem_task = task().lower()
        print('What should be the time?')
        speak('What should be the time?')
        time_task = task().lower()
        print('Remind you to ' + rem_task + ' at ' + time_task + '. Confirm?')
        speak('Remind you to ' + rem_task + ' at ' + time_task + '. Confirm?')
        conf_task = task().lower()
        if 'yes' in conf_task or 'yash' in conf_task:
            print('Reminder added')
            speak('Reminder added')
            time_task = datetime.strptime(time_task.replace('.',''),'%I:%M %p')
            return rem_task,time_task
        else:
            print('No reminder added')
            speak('No reminder added')
            time_task = datetime.strptime('12:00 AM','%I:%M %p')
            return rem_task,time_task
