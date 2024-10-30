from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Your API URL
API_URL = "https://api-data.telkomiot.id/api/v2.0/APP6356c38bde5a779890/DEV63d2c0fabbbd249223/lasthistory"

# Fetch sensor data from the API
def fetch_sensor_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()  # Assuming the API returns JSON
    except requests.exceptions.RequestException as e:
        return {"error": f"Error fetching data: {str(e)}"}

@app.route('/', methods=['GET'])
def handle_request():
    data = fetch_sensor_data()
    if "error" in data:
        return jsonify(data), 500
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
