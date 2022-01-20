import question_answering_model as fl
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import description as ds


class Item(BaseModel):
    question: str
    paragraph: str

class sequel(BaseModel):
    text: str
    max_length: int
    temperature: Optional[float] = 0.7
        

app = FastAPI(
    title="URFU Text Working API",
    description=ds.description,
    openapi_tags=ds.tags_metadata,
    version="0.2",
    license_info={
        "name": "Common Public License",
        "url": "https://opensource.org/licenses/cpl1.0.php",
    }
)


@app.get("/", tags=["Запрос на доступность"])
async def root():
    return "This is a question answering model"

@app.post("/predict_ans/", tags=["Вопрос|Ответ"])
async def predict(item: Item):
    return fl.answer_question(item.question, item.paragraph)

#@app.post("/predict_sequel/", tags=["Перефразирование"])
#async def predict_sequel(sequel: sequel):
#    return fl.generate_text(sequel.text, sequel.max_length, sequel.temperature)

@app.post("/predict_cap/", tags=["Преступление и наказание"])
async def predict_sequel(sequel: sequel):
    return fl.generate_cap(sequel.text, sequel.max_length, sequel.temperature)
