# Text Working API

## API, которое позволяет работать с несколькими текстовыми моделями

Развёрнуто на **Heroku**:
https://question-answering-model.herokuapp.com

### Методы:
* **/predict/** - позволяет отправить текст и вопрос к этому тексу. В ответ приходит пара вопрос|ответ.
* **/predict_cap/** - перефразирует указанный текст в другой с учетом числа символов, которые поступили в запросе.
* **/predict_sequel/** - дополняет произвольный текст цитатми из "Преступления и наказания", наиболее подходящими по смыслу.

#### Использованные готовые модели
* **/predict/** - https://tfhub.dev/see--/bert-uncased-tf2-qa/1  
* **/predict_cap/** - https://huggingface.co/google/reformer-crime-and-punishment  
* **/predict_sequel/** - https://huggingface.co/google/t5-small-lm-adapt  

#### Документация и описание параметров:
https://question-answering-model.herokuapp.com/docs

## Примеры:
### /predict/
Отправляем POST-запросом в body JSON-файлом текст и вопрос к нему:
```json
    "question" : "How much sovereign nations does Russia have?",
    "paragraph" : "Russia (Russian: Россия, Rossiya, Russian pronunciation:[rɐˈsʲijə]), or the Russian Federation,[b] is a country spanning Eastern Europe and Northern Asia. It is the largest country in the world, covering over 17,125,191 square kilometres (6,612,073 sq mi), and encompassing one-eighth of Earth's inhabitable landmass. Russia extends across eleven time zones, and has the most borders of any country in the world, with sixteen sovereign nations.[c] It has a population of 146.2 million; and is the most populous country in Europe, and the ninth-most populous country in the world. Moscow, the capital, is the largest city in Europe; while Saint Petersburg is the second-largest city and cultural centre. Russians are the largest Slavic and European nation; they speak Russian, the most spoken Slavic language, and the most spoken native language in Europe."            
```
Получаем результат:
```json
  "Question: How much sovereign nations does Russia have? Answer: sixteen"
```

Запрос - ответ через Postman:

![Снимок экрана 2021-12-23 в 02 04 17](https://user-images.githubusercontent.com/16818608/147164718-6403ca35-bd9b-4bf0-9446-33e63b9aa50c.png)

### /predict_cap/
Отправляем POST-запросом в body JSON-файлом текст и длину дополнения к нему:
```json
    "text" : "How much sovereign nations does Russia",
    "max_length" : 50
```
Получаем результат:
```json
  "How much sovereign nations does Russia was making more chin looked at the time and was except for any old-fash"
```

### /predict_sequel/
Отправляем POST-запросом в body JSON-файлом текст и длину дополнения к нему:
```json
    "text" : "The superjumbo was developed at a cost of $25 billion and, with capacity for up to 853 passengers",
    "max_length" : 200
```
Получаем результат:
```json
  "Question: How much sovereign nations does Russia have? Answer: sixteen"
```

