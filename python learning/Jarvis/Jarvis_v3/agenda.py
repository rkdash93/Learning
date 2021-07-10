from time import sleep,strftime
from datetime import datetime,date
from speak import *

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
            f = open(r"agenda.txt","a")
            f.writelines("\n"+agenda_line)
            f.close()
            print("Agenda added")
            speak("Agenda added")
        else:
            print("No agenda added")
            speak("No agenda added")            

    if tsk == 'read':
        f = open('agenda.txt')
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
        if 'yes' in conf_task.lower() or 'yash' in conf_task:
            print('Reminder added')
            speak('Reminder added')
            time_task = datetime.strptime(time_task.replace('.',''),'%I:%M %p')
            return rem_task,time_task
        else:
            print('No reminder added')
            speak('No reminder added')
            time_task = datetime.strptime('12:00 AM','%I:%M %p')
            return rem_task,time_task

# agenda_func('write')