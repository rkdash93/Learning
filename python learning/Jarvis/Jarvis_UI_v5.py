import sys
import tkinter as tk
from datetime import datetime
import time
import psutil
from PIL import Image, GifImagePlugin

root = tk.Tk()
root.configure(bg='#000606')
root.geometry('800x500')

format = '%I:%M %p'
now=datetime.now()
curr_time = now.strftime(format)


#bg.pack()
file='Jarvis.gif'
#find number of frames
info = Image.open(file)
frames=info.n_frames

#create list of frames
im = [tk.PhotoImage(file=file,format=f'gif -index {i}') for i in range(frames)]

#function to iterate through list of frames
count = 0
def update(count):
    im2 = im[count]
    label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    root.after(100,lambda:update(count))



label = tk.Label(root,image="",borderwidth=0,bg='#000606')
label.grid(row=1)

text = tk.Text(root, height = 5, width = 100)
text.insert(tk.END,'How can I help you?')
#text.pack()

mic_img=tk.PhotoImage(file='mic-button.png')
chat_img=tk.PhotoImage(file='chatbutton.png')
time_img=tk.PhotoImage(file='jarvis_time1.png')


t_button = tk.Button(root,padx=10,image=chat_img,text = 'Type',font = ('Helvetica',12),fg='#ffffff',bd=1,bg = '#6e6a73')
s_button = tk.Button(root,padx=10,image=mic_img,text = 'speak',font = ('Helvetica',12),fg='#ffffff',bd=1,bg = '#6e6a73')


#t_button.grid(row=1,column=0,sticky=tk.NW)
#s_button.grid(row=2,column=0,sticky=tk.NW,pady=10)

label3=tk.Label(root,image=time_img,borderwidth=0,text=curr_time,font = ('Helvetica',14),fg='#ffffff',compound=tk.CENTER,)
#label3.grid(row=0,column=0)



root_user=None

def change_color():
    current_color = box.cget("fg")
    next_color = "grey" if current_color == "cyan" else "cyan"
    box.config(fg=next_color)
    root.after(1200, change_color)

def hide_frnt():
    box.grid_forget()
    label_stup.grid_forget()
    label.grid_forget()
    button_next.grid_forget()
#    button_speak.grid_forget()
    entry_root()
   

def entry_root():
    global root_user
    root_user = entry_user.get()


box = tk.Text(root,bg = '#000606',bd=0, fg="grey",font = ('Verdana','15'),padx=10,height=5)

box.insert(tk.END,'Setting up the application for the first time.\nPlease wait....')
box.grid(row=0,sticky=tk.W)
change_color()

battery = psutil.sensors_battery()
print(battery[2])

label_stup=tk.Label(root,bg = '#000606',bd=0, fg="grey",font = ('Verdana','14'),padx=10,text='Please setup root user and passphrase')
label_stup.grid(row=1,sticky=tk.W)



mic_img=tk.PhotoImage(file='mic-button.png')

entry_user = tk.Entry(root,width=30)
entry_passphrase = tk.Entry(root,width=30) 
button_next =tk.Button(root,text='NEXT',command=hide_frnt)
label_root = tk.Label(root,text='Enter your name: ',fg = 'grey',font = ('Verdana','14'),bg = '#000606')
label_root.grid(row=2,sticky=tk.W,padx = 15)
label_root = tk.Label(root,text='Enter the passphrase: ',fg = 'grey',font = ('Verdana','14'),bg = '#000606')
label_root.grid(row=3,sticky=tk.W,padx = 15)
button_next.grid(row=4)
entry_user.grid(row=2)
entry_passphrase.grid(row=3)
root.bind('<Return>',entry_root())

print (root_user)
update(count)
root.mainloop()




#anim(count)
