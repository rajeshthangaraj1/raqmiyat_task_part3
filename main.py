import os
import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()
MODEL_PATH = os.getenv('MODEL_PATH', 'model/model.pkl')
VECTORIZER_PATH = os.getenv('VECTORIZER_PATH', 'model/vectorizer.pkl')
# LOG_FILE = os.getenv('LOG_FILE', 'logs/api.log')


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load model and vectorizer
try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    logger.info('Model and vectorizer loaded successfully.')
except Exception as e:
    logger.error(f'Error loading model/vectorizer: {e}')
    raise

# FastAPI app
app = FastAPI(title="Document Type Classifier API")

class PredictRequest(BaseModel):
    text: str

class PredictResponse(BaseModel):
    label: str

@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    try:
        logger.info(f"Received prediction request: {request.text}")
        X = vectorizer.transform([request.text])
        pred = model.predict(X)[0]
        logger.info(f"Prediction: {pred}")
        return PredictResponse(label=pred)
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail="Prediction failed.")

@app.get("/health")
def health():
    return {"status": "ok"}
