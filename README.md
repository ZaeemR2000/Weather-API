# Weather API
 This project is a Python-based command-line application that uses the OpenWeather API to fetch the current weather information for a specific city. The user has the option to input their desired city and state or use their current location based on their IP address to get real-time weather updates such as temperature, weather description (e.g., sunny, cloudy), and chances of rain.

Why I Chose OpenWeather API

    I chose the OpenWeather API for several key reasons:

    Prior Experience: Having used OpenWeather in previous projects, I am familiar with its structure, endpoints, and response formats. This familiarity significantly reduces the learning curve and allows me to implement the weather features more efficiently.

    Simple Access and Setup: OpenWeather API provides a hassle-free process to obtain an API key, requiring minimal verification and no payment details upfront. This made it a convenient choice when I needed a quick and easy solution.

    Free Tier Generosity: OpenWeather offers a free tier that allows up to 1,000 API calls per day, which is more than enough for my project's requirements. This ensures I can make real-time weather requests without worrying about hitting any usage limits or needing to pay for additional API calls.

    No Cost: As a developer working on a small-scale project, it was essential to use an API that didn’t require any upfront costs. OpenWeather provides a robust free tier with all the necessary data (temperature, weather conditions, rain probability), making it a perfect fit for this project without any financial burden.


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