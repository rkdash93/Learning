from speak import *

def agenda_func(task):
    if task == 'write':
        print('What should I add?')
        speak('What should I add?')
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
                agenda_line = cmd
                cmd = 'Should I add ' + cmd
                print(cmd)
                speak(cmd)
                with sr.Microphone() as source:
                    playsound(speech_audio)
                    print('Listening....')
                    r.adjust_for_ambient_noise(source)
                    r.pause_threshold = 1
                    audio = r.listen(source)
                    try:
                        cmd = r.recognize_google(audio,key=GOOGLE_API_KEY,language='en-in')
                        print(cmd)
                        if cmd.lower() == 'yes':
                            f = open(r"agenda.txt","a")
                            f.writelines("\n"+agenda_line)
                            f.close()
                            print("Agenda added")
                            speak("Agenda added")
                        else:
                            print("No agenda was added")
                            speak("No agenda was added")
                    except Exception as e:
                        print('No agenda was added')
                        speak('No agenda was added')                            
            except Exception as e:
                pass

    if task == 'read':
        print('You have following agenda for today')
        speak('You have following agenda for today')
        f = open('agenda.txt')
        agenda = f.read()
        print(agenda)
        speak(agenda)
        f.close()

    return(1)                   