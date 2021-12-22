import question_answering_model as fl
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    question: str
    paragraph: str
        

app = FastAPI()


@app.get("/")
async def root():
    return "This is a question answering model"

@app.post("/predict/")
def predict(item: Item):
    return fl.answer_question(item.question, item.paragraph)
