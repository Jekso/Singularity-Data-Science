from sklearn.externals import joblib 
  

model = joblib.load('model.pkl') 
print(model.predict([[10.5]])[0])