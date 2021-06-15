import psutil
import time
import pyttsx3
from pyttsx3.drivers import sapi5
import tkinter as tk

root = tk.Tk()
root.title('BatMon')
root.configure(bg='#000606')
root.geometry('500x300')


img_path='D:\python learning\project\\battery_monitor\\batmon.png'
img=tk.PhotoImage(file=img_path)

label = tk.Label(root,image=img,bd=0)
label.pack()

label_info = tk.Label(root,text='Monitoring....',height=3,font=('Verdana',11),fg='white',bg='#000606')

label_per = tk.Label(root,height=3,width=20,font=('Verdana',9),fg='white',bg='#000606')



engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()




def monitor():
    label_info.pack(pady=5)
    label_per.pack(pady=10,anchor=tk.S)
    
    #button.pack_forget()
    
    while True:
        root.update()
        #time.sleep(10)
        battery = psutil.sensors_battery()
        percent='Battery percentage: ' + str(battery[0])
        #print(type(percent))
        if (battery[0] <= 10 and battery[2] == False):
            label_per.configure(text='Battery Percentage : ' + str(battery[0]) + '%')
            label_per.update()
            label_info.configure(text='Battery percentage is below 10 percent. Please plugin the charger')
            label_info.update()
            speak('Battery percentage is above 10 percent. Please plugin the charger')
            time.sleep(300)
        elif (battery[0] == 90):
            label_per.configure(text='Battery Percentage : ' + str(battery[0]) + '%')
            label_per.update()           
            label_info.configure(text='Battery is fully charged. Please remove the charger')
            label_info.update()
            speak('Battery percentage is above 90 percent')
            time.sleep(900)
        elif (battery[0] == 100 and battery[2] == True):
            label_per.configure(text='Battery Percentage : ' + str(battery[0]) + '%')
            label_per.update()
            label_info.configure(text='Battery is fully charged. Please remove the charger')
            label_info.update()
            speak('Battery is fully charged. Please remove the charger')
            root.update()
            time.sleep(10)
        else:
            label_per.configure(text='Battery Percentage : ' + str(battery[0]) + '%')
            label_per.update()            
            label_info.configure(text='Monitoring...')
            label_info.update()                                  
        #root.mainloop()


button = tk.Button(root,text='Turn On',command=monitor)
#button.pack(pady=80,anchor=tk.S)
#root.after(1000,monitor1)
monitor()
#root.mainloop()

