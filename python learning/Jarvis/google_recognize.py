import speech_recognition as sr
import pyttsx3

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    speak('Hello user!')
    take_cmd()


def take_cmd():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f'{statement}\n')
            if 'how are you doing' in statement:
                speak('I am doing great. Thanks!')
                print('I am doing great. Thanks!')        
        except:
            speak('I do not understand')
            print('I do not understand')

greet()
#take_cmd()