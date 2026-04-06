from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get symptoms from form
        symptoms = [
            int(request.form.get('fever', 0)),
            int(request.form.get('cough', 0)),
            int(request.form.get('headache', 0)),
            int(request.form.get('fatigue', 0)),
            int(request.form.get('nausea', 0)),
            int(request.form.get('vomiting', 0)),
            int(request.form.get('chest_pain', 0)),
            int(request.form.get('shortness_breath', 0))
        ]

        # Predict
        prediction = model.predict([symptoms])[0]
        probability = model.predict_proba([symptoms]).max() * 100

        return render_template('result.html', disease=prediction, probability=round(probability, 2))

    return render_template('predict.html')

@app.route('/result')
def result():
    return render_template('result.html')

# Export the Flask app as WSGI application for Vercel
application = app