import sys
import tkinter as tk
from datetime import datetime
import time
import psutil
from PIL import Image, GifImagePlugin

root_pg1 = tk.Tk()
root_pg1.configure(bg='#000606')
root_pg1.geometry('800x450')
bgimg='jarvis_bg.png'

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
    root_pg1.after(100,lambda:update(count))



label = tk.Label(root_pg1,image="",borderwidth=0,bg='#000606')
label.grid(row=0,column=1)

def change_color():
    current_color = box.cget("fg")
    next_color = "grey" if current_color == "cyan" else "cyan"
    box.config(fg=next_color)
    root_pg1.after(1200,change_color)


def dest_root_pg1():
    root_pg1.destroy()    

box = tk.Text(root_pg1,bg = '#000606',bd=0, fg="grey",font = ('Verdana','15'),padx=10,height=5,width=30)
box.insert(tk.END,'Hello User, please press the next \nbutton to set up root user and \npassphrase')
box.grid(row=0,column=0)


button_next =tk.Button(root_pg1,text='Next',command=dest_root_pg1)
button_next.grid(sticky=tk.S)
change_color()
update(count)
root_pg1.mainloop()




root1 = tk.Tk()
root1.configure(bg='#000606')
root1.geometry('800x350')
root_user = None
passphrase = None


def change_color():
    current_color = box.cget("fg")
    next_color = "grey" if current_color == "cyan" else "cyan"
    box.config(fg=next_color)
    root1.after(1200, change_color)

def hide_frnt():
    box.grid_forget()
    label_stup.grid_forget()
    #label.grid_forget()
    button_next.grid_forget()
    entry_user.grid_forget()
    entry_passphrase.grid_forget()
    global root_user
    root_user = entry_user.get()

def dest_root1():
    global root_user
    global passphrase
    root_user = entry_user.get()
    passphrase = entry_passphrase.get()
    root1.destroy()
   

def entry_root():
    global root_user
    global passphrase
    root_user = entry_user.get()
    passphrase = entry_passphrase.get()


box = tk.Text(root1,bg = '#000606',bd=0, fg="grey",font = ('Verdana','15'),padx=10,height=5)

box.insert(tk.END,'Setting up the application for the first time.\nPlease wait....')
box.grid(row=0,sticky=tk.W)
change_color()

battery = psutil.sensors_battery()
print(battery[2])

label_stup=tk.Label(root1,bg = '#000606',bd=0, fg="grey",font = ('Verdana','14'),padx=10,text='Please setup root user and passphrase')
label_stup.grid(row=1,sticky=tk.W)



mic_img=tk.PhotoImage(file='mic-button.png')

entry_user = tk.Entry(root1,width=30)
entry_passphrase = tk.Entry(root1,width=30) 
button_next =tk.Button(root1,text='Confirm',command=dest_root1)
label_root = tk.Label(root1,text='Enter your name: ',fg = 'grey',font = ('Verdana','14'),bg = '#000606')
label_root.grid(row=2,sticky=tk.W,padx = 15)
label_root = tk.Label(root1,text='Enter the passphrase: ',fg = 'grey',font = ('Verdana','14'),bg = '#000606')
label_root.grid(row=3,sticky=tk.W,padx = 15)
button_next.grid(row=4)
entry_user.grid(row=2)
entry_passphrase.grid(row=3)
#root.bind('<Return>',entry_root())

print (root_user)
#update(count)
root1.mainloop()
print (root_user)
print(passphrase)






#anim(count)
