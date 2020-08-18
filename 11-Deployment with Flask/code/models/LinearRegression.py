import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib 
  

# import data
data_set = pd.read_csv('Salary_Data.csv')
x = data_set['YearsExperience'].values.reshape(-1, 1)
y = data_set['Salary']

# split data to training set and testing set
x_train, x_test, y_train, y_test = train_test_split(x, y)

# training the data
model = LinearRegression()
model.fit(x_train, y_train)

# predicting the data
y_pred = model.predict(x_test)

# Save the model as a pickle in a file 
joblib.dump(model, 'model.pkl') 

# plot the results
plt.plot(x_train, y_train, 'ro', label='training_data')
plt.plot(x_test, y_test, 'bo', label='testing_data')
plt.plot(x_test, y_pred, 'g-', label='predicted_data')
plt.legend()
plt.show()