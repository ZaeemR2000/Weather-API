import requests

# OpenWeather and IP location APIs
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key.txt', 'r').read()

def kelvinToCelsiusFahrenheit(kelvin):
    """Convert Kelvin to Celsius and Fahrenheit."""
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

def get_current_location():
    """Get user's current location based on their IP address."""
    ipinfo_url = "http://ipinfo.io"
    try:
        response = requests.get(ipinfo_url).json()
        city = response['city']
        region = response['region']  # Can be state or country based on location
        return city, region
    except Exception as e:
        print("Unable to retrieve current location. Please enter manually.")
        return None, None

def get_weather_data(city, state):
    """Retrieve weather data for a given city and state."""
    url = f"{BASE_URL}appid={API_KEY}&q={city},{state}"
    response = requests.get(url).json()
    
    if response.get("cod") != 200:
        print("City not found or invalid API request.")
        return None
    else:
        return response

def display_weather_info(response, city):
    """Display weather information."""
    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = kelvinToCelsiusFahrenheit(temp_kelvin)
    description = response['weather'][0]['description']
    
    print(f"Temperature in {city}: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
    print(f"Weather: {description.capitalize()}")
    
    if 'rain' in response:
        rain_info = response['rain'].get('1h', 0)  # Get rain data for the past 1 hour
        print(f"Chance of rain: {rain_info} mm in the last hour")
    else:
        print("No rain data available.")

# Ask the user whether to use current location or manual input
use_current_location = input("Do you want to use your current location? (yes/no): ").strip().lower()

if use_current_location == 'yes':
    city, state = get_current_location()
    if city and state:
        response = get_weather_data(city, state)
        if response:
            display_weather_info(response, city)
else:
    # Manual input
    city = input("Enter the city: ")
    state = input("Enter the state/country code (e.g., US for the United States): ")
    
    response = get_weather_data(city, state)
    if response:
        display_weather_info(response, city)
