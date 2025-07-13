# Document Type Classifier API (Part 3)

This project serves a trained document type classifier (invoice, resume, report) as a FastAPI API.

## Setup

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Train and Save Model**
   - Run your training script from Part 2 to generate `model/model.pkl` and `model/vectorizer.pkl`.

3. **Configure Environment**
   - Edit `.env` if you want to change model or log file locations.

4. **Run the API**
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

### `POST /predict`
- **Request Body:**
  ```json
  { "text": "Your document text here" }
  ```
- **Response:**
  ```json
  { "label": "invoice" }
  ```

### `GET /health`
- Returns `{ "status": "ok" }` if the API is running.

## Logs
- Logs are written to `logs/api.log` by default.

## Docker (Optional)
- See `Dockerfile` for containerization instructions.
