import psutil
import time
import pyttsx3
from pyttsx3.drivers import sapi5
import tkinter as tk

# UI
root = tk.Tk()
root.title('BatMon')
root.configure(bg='#000606')
root.geometry('500x300')


img_path='batmon.png'
img=tk.PhotoImage(file=img_path)

label = tk.Label(root,image=img,bd=0)
label.pack()

label_info = tk.Label(root,text='Monitoring....',height=5,font=('Verdana',12),fg='white',bg='#000606')

label_per = tk.Label(root,height=3,width=100,font=('Verdana',14),fg='white',bg='#000606')



engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()



# Battery Monitor function
def monitor():
    label_info.pack(pady=5)
    label_per.pack(pady=10,anchor=tk.S)
    

    try:
        while True:
            root.update()
            battery = psutil.sensors_battery()
            plugged =' (Charging)' if battery[2]==True else ' (Not Charging)'
            #10 percent charge and not charging, alert every 2 mins
            if (battery[0] <= 10 and battery[2] == False):
                label_per.configure(text='Battery Percentage : ' + str(battery[0]) + '%' + plugged)
                label_per.update()
                label_info.configure(text='Battery percentage is below 10 percent.\nPlease plugin the charger')
                label_info.update()
                speak('Battery percentage is below 10 percent. Please plugin the charger')
                scnds = time.time() + 60 * 2
                while time.time() < scnds:
                    root.update()
                    battery = psutil.sensors_battery()
                    label_per.configure(text='Battery Percentage : ' + str(battery[0]) + '%' + plugged)
                    label_per.update()
            #20 percent charge left and not charging, one time alert                    
            elif (battery[0] == 19 and battery[2] == False):
                #speak('Battery percentage is below 20 percent. Please plugin the charger')                
                label_per.configure(text='Battery Percentage : ' + str(battery[0]) + '%' + plugged)
                label_per.update()
                label_info.configure(text='Battery percentage is below 20 percent.\nPlease plugin the charger')
                label_info.update()
                speak('Battery percentage is below 20 percent. Please plugin the charger')
                while (battery[0] == 19):
                    root.update()
                    battery = psutil.sensors_battery()
            #90 percent charged and still charging, one time alert    
            elif (battery[0] == 90 and battery[2] == True):
                label_per.configure(text='Battery Percentage : ' + str(battery[0]) + '%' + plugged)
                label_per.update()           
                label_info.configure(text='Battery percentage is above 90 percent')
                label_info.update()
                speak('Battery percentage is above 90 percent')
                while (battery[0] == 90):
                    root.update()
                    battery = psutil.sensors_battery()
            #100 percent charged and still charging, alert every 2 mins        
            elif (battery[0] == 100 and battery[2] == True):
                label_per.configure(text='Battery Percentage : ' + str(battery[0]) + '%' + plugged)
                label_per.update()
                label_info.configure(text='Battery is fully charged.\nPlease remove the charger')
                label_info.update()
                speak('Battery is fully charged. Please remove the charger')
                scnds = time.time() + 60 * 2
                while time.time() < scnds:
                    root.update()
                    battery = psutil.sensors_battery()
                    label_per.configure(text='Battery Percentage : ' + str(battery[0]) + '%' + plugged)
                    label_per.update()
                    if battery[2] == False:
                        break
            #Normal mode no alert
            else:
                label_per.configure(text='Battery Percentage : ' + str(battery[0]) + '%' + plugged)
                label_per.update()            
                label_info.configure(text='Monitoring...')
                label_info.update()
               
    except:
        pass    

#Deprecated button 
#button = tk.Button(root,text='Turn On',command=monitor)
#button.pack(pady=80,anchor=tk.S)
#root.after(1000,monitor1)

monitor()


