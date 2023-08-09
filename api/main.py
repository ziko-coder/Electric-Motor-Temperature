from fastapi import HTTPException, FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Load the saved model
with open('LR.pkl', 'rb') as file:
    saved_model = pickle.load(file)


class PredictionRequest(BaseModel):
    features: list

class PredictionResponse(BaseModel):
    prediction: float


@app.post("/predict/")
async def predict(request: PredictionRequest):
    try:
        features = np.array(request.features).reshape(1, -1)
        prediction = saved_model.predict(features)[0]
        
        response = PredictionResponse(prediction=prediction)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port='8000')
