import os
import requests

api_key = ""

lat = -55.784330
lon = 49.119810
weather_params = {
    "lat": lat,
    "lon": lon,
    "exclude": "current,minute,daily",
    "appid": api_key
}
base_url = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(base_url, params=weather_params)
response.raise_for_status()
weather_data = response.json()['list'][0]['weather'][0]['id']
if weather_data < 100:
    print("bring an umbrella")
else:
    print("wear a jacket")

print(weather_data)
