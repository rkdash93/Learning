import sys
import tkinter as tk
from PIL import Image, GifImagePlugin

root = tk.Tk()
root.configure(bg='black')
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


label = tk.Label(root,image="",borderwidth=0)
label.pack()

text = tk.Text(root, height = 5, width = 100)
text.insert(tk.END,'How can I help you?')
text.pack()


update(count)
root.mainloop()




#anim(count)
