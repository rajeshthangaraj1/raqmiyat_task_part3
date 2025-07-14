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
   - Rename `sample.env` to `.env`:
     ```bash
     mv sample.env .env
     ```
   - Edit `.env` if you want to change model or log file locations.

4. **Run the API**
   ```bash
   uvicorn main:app --reload
   ```
   - After starting the server, open your browser and go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the FastAPI interactive docs UI.
   - Here, you can use the `/predict` endpoint by entering your document text and receiving the predicted label as output.

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
