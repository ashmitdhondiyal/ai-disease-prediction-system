# AI Disease Prediction System

This is a full-stack web application for predicting diseases based on symptoms using machine learning.

## Features

- Homepage with healthcare-themed design
- Symptom selection form with 8 medical symptoms
- AI-powered disease prediction using Decision Tree classifier
- Results page with confidence scores and medical disclaimers

## Tech Stack

- Backend: Python Flask (deployed as Vercel serverless function)
- Frontend: HTML, CSS, JavaScript with TailwindCSS
- ML: Scikit-learn (Decision Tree)
- Hosting: Vercel

## Local Development

1. Install Python 3.8+
2. Install dependencies: `pip install flask scikit-learn pandas`
3. Train the model: `python train_model.py`
4. Run the app: `python app.py`

## Deployment to Vercel

The project is configured for Vercel deployment:

### Option 1: Deploy via Vercel Website
1. Go to [vercel.com](https://vercel.com)
2. Sign up/Login with GitHub
3. Click "New Project"
4. Import your GitHub repository
5. Vercel will automatically detect the Python project and deploy it

### Option 2: Deploy via Vercel CLI (if installed)
```bash
npm install -g vercel
vercel
```

## Project Structure
```
AI Disease Prediction System/
├── api/
│   └── index.py          # Vercel serverless function
├── public/
│   ├── style.css         # Custom styles
│   └── script.js         # JavaScript functionality
├── templates/
│   ├── index.html        # Homepage
│   ├── predict.html      # Symptom form
│   └── result.html       # Results page
├── vercel.json           # Vercel configuration
├── requirements.txt      # Python dependencies
├── model.pkl            # Trained ML model
├── dataset.csv          # Training data
└── README.md
```

## Usage

Open the deployed URL and:
1. View the homepage with project information
2. Click "Check Your Symptoms" to access the prediction form
3. Select symptoms from the checkboxes
4. Click "Predict Disease" to get AI-powered predictions
5. View results with confidence scores and medical disclaimers

## Important Notes

- This is for educational purposes only
- Not a replacement for professional medical advice
- Always consult healthcare professionals for medical concerns