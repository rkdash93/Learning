from datetime import datetime
from speak import speak
from api_keys import WEATHER_API_KEY
import json,requests
import urllib



def daily_task():
    hour = int(datetime.now().hour)
    date = datetime.now().strftime('%A, %d-%B-%Y')
    cityfile = open('curr_city.txt')
    CITY = cityfile.read()
    cityfile.close()

      
    
    if hour >= 0 and hour < 12:
        print('Hello user! good morning')
        speak('Hello user! good morning')
    elif hour >= 12 and hour < 18:
        print('Hello user! good afternoon')
        speak('Hello user! good afternoon')
    else :
        print('Hello user! good evening')
        speak('Hello user! good evening')

    print('Meanwhile, let me brief you about today')
    speak('Meanwhile, let me brief you about today')

    print('Today is '+date)
    speak('Today is '+date)

    if datetime.now().strftime('%A') == 'Saturday' or datetime.now().strftime('%A') == 'Sunday':
        print('Today is weekend. You dont have to login for work.')
        speak('Today is weekend. You dont have to login for work.')
    else:
        if datetime.now().hour < 11:
            print('Today is weekday. You need to login for work')
            speak('Today is weekday. You need to login for work')


    # weather outside
    # base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    # API key 
    API_KEY = WEATHER_API_KEY
    # upadting the URL
    URL = BASE_URL + "q=" + CITY + "&units=metric&appid=" + API_KEY
    # HTTP request
    try:
        response = requests.get(URL)
        # checking the status code of the request
        if response.status_code == 200:
            # getting data in the json format
            data = response.json()
            # getting the main dict block
            main = data['main']
            # getting temperature
            temperature = str(main['temp']) + ' degree celsius'
            # getting weather report
            report = data['weather']
            report = str(report[0]['description'])    

            print('Temperature outside is '+temperature)            
            speak('Temperature outside is '+temperature)
            print('Weather report is ' +report)
            speak('Weather report is ' +report)                  
    except:
        pass   

