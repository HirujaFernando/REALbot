"""
This file contains functions for additional features
"""

import requests
import wikipedia
import webbrowser

# gets weather data from openweathermap.org and return
# temperature, humidity, description in a list
def get_weather(city, country_code):
    # get weather data from website
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid=0e9d4141368e13110e68dda0d815ef90"
    response = requests.get(url)

    # when successfully received data
    if response.status_code == 200:
        data = response.json()
        # convert Kelvin to Celsius
        temperature = str(round(data['main']['temp'] - 273.15, 2))
        humidity = str(data['main']['humidity'])
        weather_description = data['weather'][0]['description']
        # print the arranged data
        return [temperature, humidity, weather_description]
    # didn't receive data
    else:
        return "Error occured when getting weather information!"

# returns a summary about something from wikipedia
def get_wikiSummary(thing):
    result = wikipedia.summary(thing)
    return result

# opens website
def website(name):
    webbrowser.open("https://" + name)
