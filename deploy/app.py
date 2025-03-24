import os
import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.responses import JSONResponse
from mangum import Mangum

app = FastAPI()

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), "prediction_model.pkl")
with open(model_path, "rb") as model_file:
    model = pickle.load(model_file)

# Request model for single prediction
class AQIInput(BaseModel):
    current_aqi_value: float

# Request model for multiple AQI values (for cities/states)
class AQIBatchInput(BaseModel):
    state: str
    city: str
    aqi_values: List[float]

# Batch AQI prediction (for city/state)
@app.post("/predict_batch")
async def predict_batch(data: AQIBatchInput):
    try:
        if not data.aqi_values:
            return JSONResponse(content={"error": "AQI values list cannot be empty"}, status_code=400)

        avg_aqi = sum(data.aqi_values) / len(data.aqi_values)
        input_data = pd.DataFrame([[avg_aqi]], columns=["Current AQI value"])
        prediction = model.predict(input_data)[0]

        result = "Hard to Live" if prediction == 1 else "Good to Live"

        return JSONResponse(
            content={
                "state": data.state,
                "city": data.city,
                "average_aqi": avg_aqi,
                "prediction": result
            },
            status_code=200
        )

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

# Correct Mangum handler initialization
handler = Mangum(app, lifespan="auto")
