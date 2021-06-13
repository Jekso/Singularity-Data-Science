import joblib
from helpers.dummies import *
from flask import Flask, render_template, request

app = Flask(__name__)

model = joblib.load('models/model.h5')
scaler = joblib.load('models/scaler.h5')



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')



@app.route('/predict', methods=['GET'])
def predict():
    all_data = request.args
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

    return render_template('prediction.html', bikes_count=bikes_count)









if __name__ == "__main__":
    app.run()