import joblib
from helpers.dummies import *
from flask import Flask, jsonify, request

app = Flask(__name__)

model = joblib.load('models/model.h5')
scaler = joblib.load('models/scaler.h5')


@app.route('/predict', methods=['POST'])
def predict():
    all_data = request.json
    temp = float(all_data['temp'])
    humidity = float(all_data['humidity'])
    month = int(all_data['datetime'].split('-')[1])
    hour = int(all_data['datetime'].split('T')[1].split(':')[0])
    is_rush_hour = int(all_data['is_rush_hour'])
    season = season_dummies[all_data['season']]
    weather = weather_dummies[all_data['weather']]
    weekday = weekdays_dummies[all_data['weekday']]
    pod = pod_dummies[all_data['peroid_of_day']]

    x = [temp, humidity, hour, is_rush_hour, month]
    x += season + weather + weekday + pod


    x = scaler.transform([x])
    bikes_count = round(model.predict(x)[0])

	return jsonify({"bikes_count": bikes_count})




if __name__ == "__main__":
    app.run(debug=True)
