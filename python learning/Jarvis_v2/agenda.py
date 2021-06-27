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
