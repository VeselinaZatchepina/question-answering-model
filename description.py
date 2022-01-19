description = """
URFU_TextApp API поможет использовать ML для решения задач с текстами. 🚀

## Методы

В API есть два метода:
* /predict_ans/ - позволяет отправить текст и вопрос к этому тексу. В ответ приходит пара вопрос|ответ.
* /predict_cap/ - перефразирует указанный текст в другой с учетом числа символов, которые поступили в запросе.

## Авторы

* Веселина Зацепина
* Цинцов Никита
* Констатин Кожемяков

Лицензия:
"""

tags_metadata = [
    {
        "name": "Вопрос|Ответ",
        "description": "Находит ответ в тексте",
        "externalDocs": {
            "description": "TF.HubModel",
            "url": "https://tfhub.dev/see--/bert-uncased-tf2-qa/1",
        },
    },
    {
        "name": "Преступление и наказание",
        "description": "Продолжает текст походящей цитатой из книги",
        "externalDocs": {
            "description": "HF.model",
            "url": "https://bit.ly/3Ilck7L",
        },
    },
        #{
        #"name": "Перефразирование",
        #"description": "Перефразирует текст в другой",
        #"externalDocs": {
        #    "description": "HF.model",
        #    "url": "https://bit.ly/3GHSuCW",
        #},
    #},
    {
        "name": "Запрос на доступность",
        "description": "Выдает дефолтный ответ, если API доступно",

    },
]
