
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
  
root = Tk()
root.title("Funedit")
icon_img = ImageTk.PhotoImage(Image.open(".\\images\\notepad_icon.ico"))

root.geometry("700x350")

root.attributes('-topmost', True)
root.iconphoto(True,icon_img)

  
count = 0

# adding scrollbar
scrollbar = Scrollbar(root)
  
# packing scrollbar
scrollbar.pack(side=RIGHT,
               fill=Y)
  
 
text_info = Text(root,
                 yscrollcommand=scrollbar.set)
text_info.pack(fill=BOTH)

  
# configuring the scrollbar
scrollbar.config(command=text_info.yview)

def key_press(e):
    global count
    fun_str = [" ",".","l","o","o","f"," ","a"," ","m","a"," ","I"]
    if count == 13:
        count = 0
    else:
        # print("count:",count)
        # print(fun_str[count])
        text_info.insert("1.0",fun_str[count])
        count += 1

    text_info.delete("end-2c","end")



def on_closing():       
    if messagebox.askokcancel("Close", "I agree that I am a fool"):
        messagebox.showinfo(title=None,message="As you have confirmed. You are a Fool")
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# # Bind the key event
root.bind('<KeyPress>',key_press)
  
root.mainloop()

