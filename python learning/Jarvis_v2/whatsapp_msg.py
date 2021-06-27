from datetime import datetime
from speak import speak
import pywhatkit as kit

def send_shop():
    now = datetime.now()
    #print(now.minute)

    f = open('shopping_list.txt','r')
    shopping_list = f.readlines()[0:]
    text_str = ''
    for line in shopping_list:
    #if time > line.rstrip():
    #    today = 1
        text_str = text_str + line       
    f.close()
    #print(text_str)

    try:
        kit.sendwhatmsg("+919437163256",text_str,now.hour,int(now.minute + 1))
        print('Message sent')
    except:
        print('Error')

def read_shop():
        print('Here is your shopping list')
        speak('Here is your shopping list')
        f = open('shopping_list.txt','r')
        s_list = f.read()
        print(s_list)
        speak(s_list)
        f.close()            

#send_shop() 