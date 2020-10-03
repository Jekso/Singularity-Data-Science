from flask import Flask, jsonify, request
import joblib

# __name__ is equal to app.py
app = Flask(__name__)

# load model from model.pck
model = joblib.load('model.pkl')


@app.route("/predict", methods=["POST"])
def predict():
	tempreture =  request.json['Tempreture']
	humadity =  request.json['Humadity']
	wind =  request.json['Wind']
	season =  request.json['Season']

	if season == 'winter':
		is_spring = 0
		is_summer = 0
		is_winter = 1
	elif season == 'summer':
		is_spring = 0
		is_summer = 1
		is_winter = 0
	elif season == 'spring':
		is_spring = 1
		is_summer = 0
		is_winter = 0
	else:
		is_spring = 0
		is_summer = 0
		is_winter = 0

	bike_count = int(round(model.predict([[tempreture, humadity, wind, is_spring, is_summer, is_winter]])[0]))
	return jsonify({"bike_count": bike_count})




if __name__ == "__main__":
    app.run(debug=True)
