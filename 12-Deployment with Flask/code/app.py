from flask import Flask, render_template, request
from sklearn.externals import joblib 
  

app = Flask(__name__)


@app.route("/")
def list():
    return render_template("index.html")


@app.route('/predict', methods=["POST"])
def predict():
    exp_years = float(request.form['exp_years'])
    model = joblib.load('models/model.pkl')
    result = int(model.predict([[exp_years]])[0])
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run()
