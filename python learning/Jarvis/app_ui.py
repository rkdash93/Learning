from tkinter import *
from PIL import Image, GifImagePlugin


root = Tk()
file = 'D:\\python learning\\Jarvis.gif'
info = Image.open(file)
frames = info.n_frames
print(frames)
im = [PhotoImage(file=file,format=f'gif -index {i}') for i in range(frames)]

count = 0
def anim(count):
    im2 = im[count]
    Label(root, image=file)
    label.configure(image=im2)
    count += 1
    label.pack()
    if count == frames:
        count = 0
    root.after(0,anim(count))




anim(count)