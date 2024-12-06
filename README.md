# Weather App

This simple Python application fetches weather data for a specified city using the OpenWeatherMap API. It displays key weather information in a human-readable format, including temperature, humidity, wind speed, and sunrise/sunset times.

## Features

- Fetches real-time weather data from the OpenWeatherMap API.
- Converts temperature from Kelvin to both Celsius and Fahrenheit.
- Displays weather information including temperature, humidity, wind speed, and more.

## Setup

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/sunilmakkar/weather-app.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenWeatherMap API key as an environment variable:
   * On macOS/Linux:
     ```bash
     export OPENWEATHER_API_KEY="your-api-key-here"
     ```

4. Run the application:
   ```bash
   python main.py
   ```

## Example Output

```
Temperature in New York: 1.37°C or 34.47°F
Temperature in New York feels like: -4.98°C or 23.04°F
Humidity in New York: 53%
Wind Speed in New York: 9.26m/s
General Weather in New York: clear sky
Sun rises in New York: 2024-12-05 12:05:17+00:00 local time.
Sun sets in New York: 2024-12-05 21:28:47+00:00 local time.
```

## Potential Improvements

This project offers several exciting opportunities for enhancement:

### 1. Simple Improvement: City Search History
- Add functionality to save and quickly recall recently searched cities
- Implement using a simple text file or JSON storage
- Makes the app more convenient for repeat users

### 2. Natural Extension: Weather Forecast
- Extend the current API integration to fetch a 5-day weather forecast
- Display predicted temperatures and conditions for upcoming days
- Requires minimal modifications to the existing code structure
- Leverages additional OpenWeatherMap API endpoints

## Notes

* Ensure that your OpenWeatherMap API key is valid.
* This project is meant for learning purposes and is kept simple to focus on best practices and code quality.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
