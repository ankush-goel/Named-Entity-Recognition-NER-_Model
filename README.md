# Named Entity Recognition (NER) API

This repository contains an NER model trained on a publicly available dataset and deployed using FastAPI.

## 🚀 Steps to Run

1. **Install dependencies**:

2. **Train the Model** (run in `notebooks/ner_training.ipynb`):
- This will generate `models/ner_model.pkl`

3. **Run the API**:

4. **Test the API**:

curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d '{"text": "Barack Obama was the 44th President of the United States."}'


## 📂 Files
- `notebooks/ner_training.ipynb`: Model training and evaluation
- `app/app.py`: API for NER predictions
- `Dockerfile`: Docker containerization setup
