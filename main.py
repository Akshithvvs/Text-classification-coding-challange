from fastapi import Body, FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from joblib import load

class InputModel(BaseModel):
    new_data: List[str]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, you can specify the domains you want to allow here
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

gl_loader = {}

@app.on_event('startup')
def load_model():
    gl_loader['logestic_model'] = load('logReg.pkl')
    gl_loader['vectorizer'] = load('tfidf_vectorizer.pkl')

@app.post("/logistics")
def logisticreg(data: InputModel) :
    if data is not None: 
        new_data_tfidf = gl_loader['vectorizer'].transform(data.new_data)
        predictions = gl_loader['logestic_model'].predict(new_data_tfidf)
        print(predictions)
    
    return {
        "predictions": predictions.tolist(),
    }

@app.get("/")
def default_func():
    return {"Hello": "World"}

