import tkinter as tk
import random
import threading
from time import sleep
from PIL import Image,ImageTk
from playsound import playsound

root = tk.Tk()
# window icon image
icon_img = ImageTk.PhotoImage(Image.open(".\\images\\slot_icon.jpg"))
root.configure(background="#04020d")
root.title("$$$ CASINO SLOT GAME $$$")
root.resizable(False,False)
root.iconphoto(True,icon_img)

# inital credit
coin = 100

# sound on off flag
m_flg = 1

# load images
start_img = ImageTk.PhotoImage(Image.open(".\\images\\default_slot.jpg"))
logo_img = ImageTk.PhotoImage(Image.open(".\\images\\slot_logo_header.jpg"))
reset_butn_img = ImageTk.PhotoImage(Image.open(".\\images\\top_up.jpg"))
root.spin_img = ImageTk.PhotoImage(Image.open(".\\images\\start_spin_red.jpg"))
root.coin_img = ImageTk.PhotoImage(Image.open(".\\images\\coin_img.png"))
root.sound_img = ImageTk.PhotoImage(Image.open(".\\images\\sound_img.jpg"))
root.mute_img = ImageTk.PhotoImage(Image.open(".\\images\\sound_img_mute.jpg"))
root.cashout_img = ImageTk.PhotoImage(Image.open(".\\images\\cashout.jpg"))  


# labels
scorebar = tk.Label(root,text=f"Credit: ${coin}",fg="#9c2cb5",font=("Arial",12,"bold"),bg="#04020d")
header = tk.Label(root,image=logo_img,fg="white",font=("Arial",10,"bold"),bg="#04020d")
header2 = tk.Label(root,text="Place Bet!!!",fg="#9c2cb5",font=("Arial",12,"bold"),bg="#04020d")
l1 = tk.Label(root,image=start_img,bg="#04020d")
footer = tk.Label(root,text="Try your luck!!!",fg="#85e3f8",font=("Arial",12,"bold"),bg="#04020d",bd=2)

# Placing labels
header.grid(row=1,column=1,columnspan=3)
scorebar.grid(row=2,column=1)
header2.grid(row=2,column=2)
l1.grid(row=3,columnspan=3,column=1)



none_list = ["none.jpg","none2.jpg","none3.jpg","none4.jpg","none5.jpg","none6.jpg"]
jackpot_list = ["jackpot1.jpg","jackpot2.jpg","jackpot3.jpg"]
partial_list = ["beer_partial.jpg","beer_partial2.jpg","beer_partial3.jpg","beer_partial4.jpg",
"beer_partial5.jpg","beer_partial6.jpg","flower_partial.jpg","flower_partial2.jpg","flower_partial3.jpg",
"pot_partial.jpg","pot_partial2.jpg","pot_partial3.jpg","pot_partial4.jpg","pot_partial5.jpg","pot_partial6.jpg",]
img_list = none_list + jackpot_list + partial_list

# counter variable
cnt=1

# Function to move image
def mvimg():
    """Method to start the spin and decide the outcome"""

    # play music based on music flag
    if m_flg == 1:
        thread = threading.Thread(target=scroll_music)
        thread.start()

    # Disable spin button if already in progress     
    play_butn["state"] = tk.DISABLED
    
    # spin code
    global cnt
    if cnt==10:
        cnt=1
    try:
        while cnt<10:
            img = random.choice(img_list)
            root.img = ImageTk.PhotoImage(Image.open(f".\\images\\{img}"))
            l1.config(image=root.img)
            l1.update()
            cnt+=1
        
        root.jobid = root.after(50,mvimg)
        # stop changing image after jobid reaches multiple of 50
        jobid_num = int(root.jobid[-2:].replace("#",""))

        # if jobid_num != 0 and jobid_num % 50 == 0:
        #     # print(jobid_num)  # Enable for debugging
        #     root.after_cancel(root.jobid)

        if jobid_num != 0 and jobid_num % 50 == 0:
            # print(jobid_num)  # Enable for debugging
            root.after_cancel(root.jobid)
            play_butn["state"] = tk.DISABLED
            coin_butn["state"] = tk.NORMAL
            # 3 matches
            if img in jackpot_list:
                # print("JACKPOT")
                header2.config(text="You won: $50")
                footer.config(text="$$$ JACKPOT $$$",fg="#ae33f5")
                coin_val(50, 2)
            # 2 matches
            elif img in partial_list:
                # print("Partially lucky")
                header2.config(text="You won: $5")
                footer.config(text="$ Cheers $")
                coin_val(5, 0)
            # No matches    
            else:           
                # print("Better Luck next time")
                header2.config(text="You won: $0")
                footer.config(text="Better Luck next time :(")
                cashout_butn["state"] = tk.NORMAL            
    except:
        pass

def reset_game():
    """ Method to restart game """
    global coin
    coin = 100
    reset_butn.grid_forget()
    footer.config(text="Try your luck!!!")
    l1.config(image=start_img)
    scorebar.config(text=f"Credit: ${coin}")
    header2.config(text="Place bet!!!")
    
    # Enable insert coin button
    coin_butn["state"] = tk.NORMAL
    if m_flg == 1:
        thread = threading.Thread(target=scroll_music)
        thread.start()

def coin_val(val,start):
    """Method to insert coin and enable spin button"""
    
    global coin
    # print(coin) # Enable for debugging
    
    coin += val
    scorebar.config(text=f"Credit: ${coin}")
    scorebar.update()
    cashout_butn["state"] = tk.NORMAL
    cashout_butn.grid(row=5,column=2)
    

    # after coin isert
    if int(start) == 1:
        coin_butn["state"] = tk.DISABLED
        header2.config(text=f"Bet: ${abs(val)}",fg="#ae33f5")
        header2.update()
        footer.config(text="Press the spin button")
        footer.update()        
        if m_flg == 1:
            playsound(".\\sound\\insert_coin.mp3")
        play_butn["state"] = tk.NORMAL

    # after spin and 2 match outcome   
    elif int(start) == 0:
        header2.config(text="Place Bet!!!",fg="#9c2cb5")
        if m_flg == 1:
            playsound(".\\sound\\win_coin.mp3")

    # after spin and 3 match outcome 
    elif int(start) == 2:
        if m_flg == 1:
            playsound(".\\sound\\jackpot.mp3")
            playsound(".\\sound\\win_coin.mp3")

    # out of coins                
    if coin < 0:
        if m_flg == 1:
            playsound(".\\sound\\no_coin.wav")
        header2.config(text="You are out of coins!!")
        header.update()
        footer.config(text="Press top-up button")
        footer.update()
        play_butn["state"] = tk.DISABLED
        coin_butn["state"] = tk.DISABLED
        cashout_butn.grid_forget()
        reset_butn.grid(row=5,column=2)

def cashout_sound():
    playsound(".\\sound\\Cash-register-sound.wav")

def scroll_music():
    """ Method for starting sound """
    playsound(".\\sound\\scroll.mp3")

def lever_action():
    """ Method to initiate lever action before the spin """
    cashout_butn["state"] = tk.DISABLED
    root.lever_img = ImageTk.PhotoImage(Image.open(".\\images\\slot_spin.jpg"))
    l1.config(image=root.lever_img)
    l1.update()
    footer.config(text="Spinning")
    footer.update()
    if m_flg == 1:
        playsound(".\\sound\\lever.mp3")    
    sleep(0.1)
    mvimg()

def toggle_music():
    global m_flg
    if m_flg == 0:
        m_flg = 1
        sound_button.config(image=root.sound_img)
    else:
        m_flg = 0
        sound_button.config(image=root.mute_img)


def resume_game(root_cashout):
    """ Method to resume game """
    # unhide parent window
    root.deiconify()
    # kill quit window
    root_cashout.destroy()

def quit_game(root_cashout):
    """ Method to quit game """
    # kill windows
    root_cashout.destroy()
    root.destroy()    


def cash_out():
    """Method for quitting the game with current balance"""
    if m_flg == 1:
        thread = threading.Thread(target=cashout_sound)
        thread.start()

    root_cashout = tk.Tk()
    
    root_cashout.geometry("350x300")
    root_cashout.configure(background="#04020d")
    root_cashout.title("$$$ CASINO SLOT GAME $$$")
    root_cashout.resizable(False,False)
    
    # # Logo label
    # logo_img1 = tk.PhotoImage(file=r".\\slot_logo2.jpg")
    # header1 = tk.Label(root_cashout,image=logo_img1,fg="white",font=("Arial",10,"bold"),bg="#04020d")
    # header1.pack()

    # thank you level   
    quit_lbl = tk.Label(root_cashout,text=f"Thank you for playing casino slot game!!!\n\nYou have credit balance of ${coin}",fg="#9c2cb5",font=("Arial",12,"bold"),bg="#04020d",bd=2)
    quit_lbl.pack(pady=40)
    quit_conf = tk.Label(root_cashout,text=f"Do you want to quit?",fg="#85e3f8",font=("Arial",12,"bold"),bg="#04020d",bd=2)
    quit_conf.pack()    

    # quit button
    quit_frame=tk.Frame(root_cashout,width=200,height=40,bg="#04020d")
    quit_frame.pack(pady=10)

    no_butn=tk.Button(quit_frame,text='No',fg="#85e3f8",bg="#04020d",font=("Arial",12,"bold"),bd=0,command=lambda:resume_game(root_cashout),cursor="hand2")
    no_butn.pack(side=tk.RIGHT,padx=30)
    yes_butn=tk.Button(quit_frame,text='Yes',fg="#85e3f8",bg="#04020d",font=("Arial",12,"bold"),bd=0,command=lambda:quit_game(root_cashout),cursor="hand2")
    yes_butn.pack(side=tk.RIGHT,padx=30)
    
    # quit_butn = tk.Button(root_cashout,text="Quit",command=lambda:root_cashout.destroy())
    # quit_butn.pack()
    # Kill parent window
    root.withdraw()
    #child mainloop
    root_cashout.mainloop()
    



# buttons
reset_butn = tk.Button(root,image=reset_butn_img,bg="#04020d",bd=0,command=reset_game)
play_butn = tk.Button(root,image=root.spin_img,command=lever_action,bg="#04020d",bd=0,cursor="hand2")
play_butn["state"] = tk.DISABLED
coin_butn = tk.Button(root,image=root.coin_img,bg="#04020d",bd=0,command=lambda:coin_val(-10,1),cursor="hand2")
sound_button = tk.Button(root,image=root.sound_img,bg="#04020d",bd=0,command=toggle_music,cursor="hand2")
cashout_butn = tk.Button(root,image=root.cashout_img,bg="#04020d",bd=0,command=cash_out,cursor="hand2")

# Place buttons
sound_button.grid(row=2,column=3,padx=10,pady=10,sticky="e")
footer.grid(row=4,column=2)
coin_butn.grid(row=5,column=1)
play_butn.grid(row=5,column=3)

# start music when game is launched
thread = threading.Thread(target=scroll_music)
thread.start()

root.mainloop()