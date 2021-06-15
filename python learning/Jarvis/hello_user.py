import tkinter as tk

root = tk.Tk()
root.title('Hello User')


label = tk.Label(root,text='Hello User')


label.pack(side = tk.TOP)
root.mainloop()