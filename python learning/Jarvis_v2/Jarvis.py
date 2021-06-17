import speech_recognition as sr
import pyttsx3
from pyttsx3.drivers import sapi5
from gtts import gTTS
from playsound import playsound

class Speech():
    r = sr.Recognizer()
    speech_audio = '.\\sound\Speech On.wav'

    def speak(self,text):
        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[0].id)
        self.engine.setProperty('volume',1.0)        
        self.engine.say(text)
        self.engine.runAndWait()
    def task(self):
            speech_audio = '.\\sound\Speech On.wav'
            r1 = sr.Recognizer()
            task_dict = {'Jarvis':'Hello user! how can I help you?','how are you doing': 'I am doing good. Thanks!','who are you': 'I am Jarvis. Your voice assistant'}
            with sr.Microphone() as source:
                    
                    r1.adjust_for_ambient_noise(source)
                    audio1 = r1.listen(source)
                    playsound(speech_audio)
                    st1 = r1.recognize_google(audio1,key='AIzaSyDt-F9QddvrhHmigjv8nNJbFo_ArYl9k4c',language='en-in')
                    print(st1)
                    for k,v in task_dict.items():
                        if k == st1:
                            print(v)
                            self.speak(v)
                                
    #print(type(task_dict))
    '''
    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        st = r.recognize_google(audio,key='AIzaSyDt-F9QddvrhHmigjv8nNJbFo_ArYl9k4c',language='en-in')
        print(st)
                                       

        
l = Speech()
while True:
    try:
        with sr.Microphone() as source:
            #r.adjust_for_ambient_noise(source)
            audio = l.r.listen(source)
            st = l.r.recognize_google(audio,key='AIzaSyDt-F9QddvrhHmigjv8nNJbFo_ArYl9k4c',language='en-in')
            print(st)
            
            if 'Jarvis' in st:
                l.speak('Hello user! how can I help you?')
                print('Hello user! how can I help you?')
                l.task()
    except:
        pass            

'''
l = Speech()
#l.speak('bura na mano holi hai')
tts=gTTS('bura na mano holi hai')
tts.save('dialogue.mp3')
playsound('dialogue.mp3')

            
                                
