import os
import tensorflow as tf
import tensorflow_hub as hub
from transformers import BertTokenizer


def main():
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    model = hub.load('bert-uncased-tf2-qa_1')
    questions = ['What\'s the second-largest city of Russia?', 'How much sovereign nations does Russia have?']
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

    for question in questions:
        question_tokens = tokenizer.tokenize(question)
        paragraph_tokens = tokenizer.tokenize(paragraph)
        tokens = ['[CLS]'] + question_tokens + ['[SEP]'] + paragraph_tokens + ['[SEP]']
        input_word_ids = tokenizer.convert_tokens_to_ids(tokens)
        input_mask = [1] * len(input_word_ids)
        input_type_ids = [0] * (1 + len(question_tokens) + 1) + [1] * (len(paragraph_tokens) + 1)

        input_word_ids, input_mask, input_type_ids = map(lambda t: tf.expand_dims(
            tf.convert_to_tensor(t, dtype=tf.int32), 0), (input_word_ids, input_mask, input_type_ids))
        outputs = model([input_word_ids, input_mask, input_type_ids])
        # using `[1:]` will enforce an answer. `outputs[:][0][0]` is the ignored '[CLS]' token logit.
        short_start = tf.argmax(outputs[0][0][1:]) + 1
        short_end = tf.argmax(outputs[1][0][1:]) + 1
        answer_tokens = tokens[short_start: short_end + 1]
        answer = tokenizer.convert_tokens_to_string(answer_tokens)
        print(f'Question: {question}')
        print(f'Answer: {answer}')


if __name__ == '__main__':
    main()
