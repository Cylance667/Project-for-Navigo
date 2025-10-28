from timezonefinder import TimezoneFinder #Timezone library
import requests
import reverse_geocoder as rg
from dotenv import load_dotenv
import os
from datetime import date, timedelta
import json
import requests
import pycountry


# Setup and initialize APIs
def initialize():
    load_dotenv()
        
    global perplexity_api
    perplexity_api = os.getenv("PERPLEXITY_API_KEY")

    global weather_api_key
    weather_api_key = os.getenv("METEO_SOURCE_API")

# Convert lat/lon -> country code
def get_country_code(latitude, longitude):
    location = rg.search((latitude, longitude))[0]
    country_code = location['cc']
    return country_code

# Convert country code to country name. Example usage: US to United States
def get_country_name(country_code):
    """
    Converts an ISO 3166-1 country code (alpha-2, alpha-3, or numeric)
    to its corresponding country name.
    """
    try:
        if len(country_code) == 2:
            country = pycountry.countries.get(alpha_2=country_code.upper())
        elif len(country_code) == 3 and country_code.isalpha():
            country = pycountry.countries.get(alpha_3=country_code.upper())
        elif len(country_code) == 3 and country_code.isdigit():
            country = pycountry.countries.get(numeric=country_code)
        else:
            return "Invalid country code format"

        if country:
            return country.name
        else:
            return "Country not found"
    except AttributeError:
        return "Country not found"

def lat_long_to_timezone(latitude, longitude):
    try:
        latitude, longitude = float(latitude), float(longitude)
        tf = TimezoneFinder()
        timezone_str = tf.timezone_at(lat=latitude, lng=longitude)
        return timezone_str

    except Exception as e:
        return "Error: " + str(e)

def get_news_with_perplexity(latitude, longitude):
    url = "https://api.perplexity.ai/chat/completions"

    payload = {
        "model": "sonar",
        "messages": [
            {
                "role": "user",
                "content": f"What is the latest news near coordinates {latitude}, {longitude}? Provide only article titles and URLs. "
                           f"I want news about politics, and economics."
            }
        ]
    }

    headers = {
        "Authorization": f"Bearer {perplexity_api}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    formated_news = []

    # Extract titles and URLs from search_results
    if 'search_results' in data:
        for result in data['search_results']:
            title = result.get('title', 'No title')
            url = result.get('url', 'No URL')
            formated_news.append({"title": title, "url": url})
        return formated_news
    return "No news found."

# Inputs the latitude and longitude and plugs that into the MeteoSource API to get the current weather for that location. 
def get_weather_for_location(latitude, longitude, unit):
    if not (unit == "Celsius" or unit == "Fahrenheit"):
        exit(f"'{unit}' is an invalid unit. Please input Celsius or Fahrenheit.")

    if unit == "Celsius":
        unit = "metric"
    elif unit == "Fahrenheit":
        unit = "us"

    parameters = {'key': weather_api_key,
                  'lat': latitude,
                  'lon': longitude,
                  'units': unit,}

    url = "https://www.meteosource.com/api/v1/free/point"

    data = requests.get(url, parameters).json()

    if not data["current"]["temperature"]:
        exit("Invalid temperature unit.")

    return {"description": data["current"]["summary"], "temperature": data["current"]["temperature"], "unit": "C" if unit == "metric" else "F"}