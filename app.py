from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from src.text_summarizer.pipeline.prediction import PredictionPipeline


text:str = "Input the text you want to summarize."

app = FastAPI()

@app.get('/', tags=['authentication'])    #default route
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")   # training route
async def train():
    try:
        os.system("python main.py")
        return Response("Training successful!")
    except Exception as e:
        return Response(f"Error occured{e}")
    
    
@app.post("/predict")       # prediction route
async def predict(text):
    try:
        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)