from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load('model.pkl')

@app.route("/")
def home():
    return render_template('index.html')



@app.route("/predict", methods=["POST"])
def predict():
    tempreture =  request.form['Tempreture']
    humadity =  request.form['Humadity']
    wind =  request.form['Wind']
    is_spring = 1 if request.form['Season'] == 'spring' else 0
    is_winter =  1 if request.form['Season'] == 'winter' else 0
    result = int(round(model.predict([[tempreture, humadity, wind, is_spring, is_winter]])[0]))
    return render_template("index.html", result=result)




if __name__ == "__main__":
    app.run()
