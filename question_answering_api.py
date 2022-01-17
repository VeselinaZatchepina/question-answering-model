import question_answering_model as fl
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    question: str
    paragraph: str
    text: str
    max_length: int
    num_return_sequences: int
        

app = FastAPI()


@app.get("/")
async def root():
    return "This is a question answering model"

@app.post("/predict/")
def predict(item: Item):
    return fl.answer_question(item.question, item.paragraph)

@app.post("/predict_sequel/")
def predict_sequel(item: Item):
    return fl.generate_text(item.text, item.max_length, item.num_return_sequences)
