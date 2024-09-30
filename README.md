# Weather API
 This project is a Python-based command-line application that uses the OpenWeather API to fetch the current weather information for a specific city. The user has the option to input their desired city and state or use their current location based on their IP address to get real-time weather updates such as temperature, weather description (e.g., sunny, cloudy), and chances of rain.

Features
    Fetches weather data for any city and state (or country) entered by the user.
    Provides the option to automatically detect the user’s current location using their IP address.
    Displays the temperature in both Celsius and Fahrenheit.
    Displays a brief weather description (e.g., sunny, cloudy, etc.).
    Shows chances of rain if available.

Installation
Clone the repository:

git clone <repository_url>
cd weather-app
Install the required dependencies. You need Python 3.x installed and the requests library:


pip install requests
Get an API key from OpenWeather by signing up and creating an account.

Save your OpenWeather API key in a file named api_key.txt in the project directory. This file should contain only the API key.

Usage
To run the program:

python weather_app.py
Program Flow:
    The program will ask if you want to use your current location. If you choose "yes", it will attempt to get your current city and state via your IP address.
    If you prefer, you can manually enter the city and state/country code.
    The program will display:
        The temperature in both Celsius and Fahrenheit.
        A description of the current weather conditions.
        Chances of rain (if available).