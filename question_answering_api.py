import question_answering_model as fl
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    question: str
    paragraph: str

class sequel(BaseModel):
    text: str
    max_length: int
    temperature: Optional[float] = 0.7
        

app = FastAPI()


@app.get("/")
async def root():
    return "This is a question answering model"

@app.post("/predict/")
async def predict(item: Item):
    return fl.answer_question(item.question, item.paragraph)

@app.post("/predict_sequel/")
async def predict_sequel(sequel: sequel):
    return fl.generate_text(sequel.text, sequel.max_length, sequel.temperature)
