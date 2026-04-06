from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as f:
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

if __name__ == '__main__':
    app.run(debug=True)

# For static site generation with Frozen-Flask
from flask_frozen import Freezer
freezer = Freezer(app)

@freezer.register_generator
def predict_generator():
    # Generate static pages for different symptom combinations
    symptoms_combinations = [
        [1,0,0,0,0,0,0,0],  # Fever only
        [0,1,0,0,0,0,0,0],  # Cough only
        [1,1,1,1,1,1,1,1],  # All symptoms
        [0,0,0,0,0,0,0,0],  # No symptoms
    ]
    for symptoms in symptoms_combinations:
        yield {'symptoms': symptoms}