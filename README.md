# GeoInfo Finder
**Input Latitude and Longitude → Get Time Zone, Local News, and Weather**

---

## Overview
GeoInfo Finder is a Python-powered web application that takes a latitude and longitude as input and returns the **time zone**, **latest local news**, and **current weather** for that location.  
It includes a simple HTML front end with a map and pin, providing an intuitive way to visualize and explore global locations.

---

## Features

### Backend (Python)
- **Time Zone Detection:** Converts latitude and longitude into the correct time zone.  
- **Local News Retrieval:** Fetches recent headlines relevant to the specified coordinates.  
- **Weather Data:** Displays temperature, conditions, and other weather information for that location.

### Front End (HTML + JavaScript + CSS)
- **Interactive Map:** Displays a globe or map with a pin marking the chosen coordinates.  
- **Latitude & Longitude Inputs:** Two text boxes for user input.  
- **Submit Button:** Sends input to the Python backend via an API call.  
- **Dynamic Display:** Shows the fetched time zone, news, and weather directly on the page.

---

## Setup Instructions

### 1. Prerequisites
- Python 3.10+
- pip (Python package manager)
- API keys for:
  - [MeteoSource](https://www.meteosource.com/)
  - [PerplexitySearch](https://www.perplexity.ai/api-platform)

---

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/geoinfo-finder.git
cd geoinfo-finder/backend

# Install dependencies
pip install -r requirements.txt

# Run the project (you can use these command or run it using your ide)
cd Frontend
python app.py
