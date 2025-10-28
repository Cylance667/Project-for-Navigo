from flask import Flask, render_template, request, jsonify
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Backend')))

import main as backend

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/process_pin", methods=["POST"])
def process_pin():
    data = request.get_json()
    lat = data.get("lat")
    lon = data.get("lon")

    try:
        # Initialize and run backend services
        backend.initialize()
        timezone = backend.lat_long_to_timezone(lat, lon)
        weather = backend.get_weather_for_location(lat, lon, "Celsius")

        # Merge results into one dictionary for JSON response
        result = {
            "timezone": timezone,
            # "news": news, ...Uncomment when news functionality is added
            "weather": weather
        }

        print("Result from backend:", result)
        return jsonify({"status": "success", "result": result}), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
