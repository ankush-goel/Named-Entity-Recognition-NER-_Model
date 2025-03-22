from fastapi import FastAPI
from pydantic import BaseModel
import spacy
import joblib

app = FastAPI()
model = spacy.load("../models/ner_model.pkl")

class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict_ner(input: TextInput):
    doc = model(input.text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return {"entities": entities}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
