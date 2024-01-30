from fastapi import Body, FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from joblib import load
from Ml.preprocessor import has_chinese_pattern


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
    gl_loader['logestic_model'] = load('Ml/logReg.pkl')
    gl_loader['vectorizer'] = load('Ml/tfidf_vectorizer.pkl')

@app.post("/logistics")
def logisticreg(data: InputModel) :
    if data is not None:
        has_chinese = any(has_chinese_pattern(item) for item in data.new_data)
        print(has_chinese)
        if not has_chinese:
            new_data_tfidf = gl_loader['vectorizer'].transform(data.new_data)
            predictions = gl_loader['logestic_model'].predict(new_data_tfidf)
            print(predictions)
        else:
            raise HTTPException(status_code=400, detail="Bad Request: Invalid text found")
        
    return {
        "predictions": predictions.tolist(),
    }

@app.get("/")
def default_func():
    return {"Hello": "World"}

