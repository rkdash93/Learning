import numpy as np
import os
import webbrowser
from speak import speak,task

# os.startfile('C:\\Program Files (x86)\\Batmon\\batmon.exe')

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


               