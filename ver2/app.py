from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np
import os


app = Flask(__name__)

# app.config['UPLOAD_FOLDER'] = 'static/'
model = pickle.load(open("predictor.pk1", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    age = int(request.form["age"])
    sex = int(request.form["sex"])
    bmi = float(request.form["bmi"])
    children = float((request.form["children"]))
    smoker = float(request.form["smoker"])
    region = float(request.form["region"])
    
    input_data = (age, sex, bmi, children, smoker, region)
    input_data_as_numpy = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy.reshape(1,-1)
    prediction = model.predict(input_data_reshaped[0])
    prediction = round(prediction,2)
    return str(prediction)