import requests,json
from api_keys import *
from speak import speak

def weather(CITY):

    # base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    # API key 
    API_KEY = WEATHER_API_KEY
    # upadting the URL
    URL = BASE_URL + "q=" + CITY + "&units=metric&appid=" + API_KEY
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = round(main['temp'])
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']
        speak('Here are the weather details for' + CITY)        
        weather_data = f"\n{CITY:-^30}\nTemperature: {temperature} degrees celsius\nHumidity: {humidity}\nPressure: {pressure}\nWeather Report: {report[0]['description']}"
        #time.sleep(2)
        return weather_data
    else:
        # showing the error message
        error_msg='Error in the HTTP request'
        return error_msg