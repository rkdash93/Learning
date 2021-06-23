
import random
from speak import *




def paheli():
    p_list = ['din may soye, raat may roye. Jitnaa roye utna khoye. Bolo kon hai ye', 'ek thaal moti say bharaa, sir kay oopar awndhaa dharaa; Jaisay jaisay thaal phiray, moti ussay ek naa geeray',
    'Aisa likhiye sabd banaaye, phal phool aur mithai ban jaaye']
    sel_p = random.choice(p_list)
    print(sel_p)
    speak(sel_p)
    speech_audio = '.\\sound\Speech On.wav'
    r = sr.Recognizer()
    with sr.Microphone() as source:
        playsound(speech_audio)
        print('Listening....')
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            cmd = r.recognize_google(audio,key=GOOGLE_API_KEY,language='en-in')
            print(cmd)
        except Exception as e:
        #print('Speak again')
            return 'None','None'
         
    return sel_p,cmd