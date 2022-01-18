# Question answering model

## Данная модель позволяет в заданном тексте найти ответ на вопрос.

### Пример:

Вводим текст:
```python
paragraph = '''<p>Russia (Russian: Россия, Rossiya, Russian pronunciation:
                    [rɐˈsʲijə]), or the Russian Federation,[b] is a country spanning
                    Eastern Europe and Northern Asia. It is the largest country in the
                    world, covering over 17,125,191 square kilometres (6,612,073 sq mi),
                    and encompassing one-eighth of Earth's inhabitable landmass. Russia
                    extends across eleven time zones, and has the most borders of any
                    country in the world, with sixteen sovereign nations.[c] It has a
                    population of 146.2 million; and is the most populous country in
                    Europe, and the ninth-most populous country in the world. Moscow,
                    the capital, is the largest city in Europe; while Saint Petersburg
                    is the second-largest city and cultural centre. Russians are the
                    largest Slavic and European nation; they speak Russian, the most
                    spoken Slavic language, and the most spoken native language in Europe.</p>'''
                  
```

Далее задаём вопросы:
```python
question = 'How much sovereign nations does Russia have?'
```

Получаем результат:
```python
Question: How much sovereign nations does Russia have?
Answer: sixteen
```

Запрос - ответ через Postman:

![Снимок экрана 2021-12-23 в 02 04 17](https://user-images.githubusercontent.com/16818608/147164718-6403ca35-bd9b-4bf0-9446-33e63b9aa50c.png)


Развёрнуто на Heroku:
http://question-answering-model.herokuapp.com
