import datetime as dt
import requests
import os

# Base URL for the OpenWeatherMap API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "New York"

if not API_KEY:
    raise ValueError("API key not found. Please set the 'OPENWEATHER_API_KEY' environment variable.")

# Temperature Converter
def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

# Use the params argument to automatically handle the query parameters
params = {
    'appid': API_KEY,
    'q': CITY
}

response = requests.get(BASE_URL, params=params).json()

# Extracting weather data and converting temperatures to Celsius/Fahrenheit
temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.fromtimestamp(response['sys']['sunrise'], tz=dt.timezone.utc)
sunset_time = dt.datetime.fromtimestamp(response['sys']['sunset'], tz=dt.timezone.utc)

# Print Statements
print(f"Temperature in {CITY}: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
print(f"Temperature in {CITY} feels like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind Speed in {CITY}: {wind_speed}m/s")
print(f"General Weather in {CITY}: {description}")
print(f"Sun rises in {CITY}: {sunrise_time} local time.")
print(f"Sun sets in {CITY}: {sunset_time} local time.")
