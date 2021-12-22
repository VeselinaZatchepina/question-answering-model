import os
import tensorflow as tf
import tensorflow_hub as hub
from transformers import BertTokenizer

class Result:
    def __init__(self, result):
        self.result = result

def getAnswer(questions, paragraph):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    model = hub.load('https://drive.google.com/drive/folders/1gJOMfdosC2CQVCpG-MHuuV986A_Of-h2?usp=sharing/bert-uncased-tf2-qa_1.tar')
   
    res = []
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
        res.append(f'Question: {question} Answer: {answer}')
    return Result(result = set(res))

