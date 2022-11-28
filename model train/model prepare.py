# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle


new = pd.read_csv("weight-height.csv")

print(new.head())

new = new.drop(['Gender'], axis=1)

X = new.iloc[:, :-1].values
y = new.iloc[:, 1].values


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=4)


model = LinearRegression()


# Train the model using the training sets
model.fit(X_train, y_train)

# Predict the response for test dataset
prediction = model.predict(X_test)
prediction = model.predict([[69.2]])


print(prediction)

# print(gnb.predict([134,644]))

filename = "fruit_model"
pickle.dump(model, open(filename, "wb"))
