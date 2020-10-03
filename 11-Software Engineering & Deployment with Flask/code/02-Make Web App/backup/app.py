from flask import Flask, render_template, request
import joblib

# __name__ is equal to app.py
app = Flask(__name__)

# load model from model.pck
model = joblib.load('model.pkl')



@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')



@app.route("/predict", methods=["POST"])
def predict():
	tempreture =  request.form['Tempreture']
	humadity =  request.form['Humadity']
	wind =  request.form['Wind']
	season =  request.form['Season']

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
	return render_template("index.html", bike_count=bike_count)	




if __name__ == "__main__":
    app.run(debug=True)
