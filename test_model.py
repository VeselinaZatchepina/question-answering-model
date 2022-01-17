from fastapi.testclient import TestClient
from question_answering_api import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "This is a question answering model"

def test_question_nations():
    response = client.post("/predict/",
        json={ 
              "question" : "How much sovereign nations does Russia have?",
	            "paragraph" : "<p>Russia (Russian: Россия, Rossiya, Russian pronunciation:[rɐˈsʲijə]), or the Russian Federation,[b] is a country spanningEastern Europe and Northern Asia. It is the largest country in the world, covering over 17,125,191 square kilometres (6,612,073 sq mi),and encompassing one-eighth of Earth's inhabitable landmass. Russia extends across eleven time zones, and has the most borders of any country in the world, with sixteen sovereign nations.[c] It has a population of 146.2 million; and is the most populous country in Europe, and the ninth-most populous country in the world. Moscow, the capital, is the largest city in Europe; while Saint Petersburg is the second-largest city and cultural centre. Russians are the largest Slavic and European nation; they speak Russian, the most spoken Slavic language, and the most spoken native language in Europe.</p>"
             }
    )
    json_data = response.json() 

    assert response.status_code == 200
    assert json_data == "Question: How much sovereign nations does Russia have? Answer: 16"
