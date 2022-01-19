import os
import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, AutoModelForCausalLM, AutoModelForSeq2SeqLM

def answer_question(question, answer_text):
    name = "mrm8488/bert-small-finetuned-squadv2"

    tokenizer = AutoTokenizer.from_pretrained(name,)

    model = AutoModelForQuestionAnswering.from_pretrained(name)
    '''
    Takes a `question` string and an `answer` string and tries to identify 
    the words within the `answer` that can answer the question. Prints them out.
    '''
    
    # tokenize the input text and get the corresponding indices
    token_indices = tokenizer.encode(question, answer_text)

    # Search the input_indices for the first instance of the `[SEP]` token.
    sep_index = token_indices.index(tokenizer.sep_token_id)

    seg_one = sep_index + 1

    # The remainders lie in the second segment.
    seg_two = len(token_indices) - seg_one
    
    # Construct the list of 0s and 1s.
    segment_ids = [0]*seg_one + [1]*seg_two

    # get the answer for the question
    start_scores, end_scores = model(torch.tensor([token_indices]), # The tokens representing our input combining question and answer.
                                    token_type_ids=torch.tensor([segment_ids]), return_dict=False) # The segment IDs to differentiate question from answer

    # Find the tokens with the highest `start` and `end` scores.
    answer_begin = torch.argmax(start_scores)
    answer_end = torch.argmax(end_scores)

    # Get the string versions of the input tokens.
    indices_tokens = tokenizer.convert_ids_to_tokens(token_indices)
    
    answer = indices_tokens[answer_begin:answer_end+1]
    #remove special tokens
    answer = [word.replace("▁","") if word.startswith("▁") else word for word in answer] #use this when using model "twmkn9/albert-base-v2-squad2"
    answer = " ".join(answer).replace("[CLS]","").replace("[SEP]","").replace(" ##","")
    
    return f'Question: {question} Answer: {answer}'


def generate_cap(text, max_length, temperature):
    #Модель Google, которая дополняет текст фразами из "Преступления и наказания"
    tok = AutoTokenizer.from_pretrained("google/reformer-crime-and-punishment")
    model = AutoModelForCausalLM.from_pretrained("google/reformer-crime-and-punishment")

    return tok.decode(model.generate(tok.encode(text, return_tensors="pt"), do_sample=True,temperature=temperature, max_length=max_length)[0])


#def generate_text(text, max_length, temperature):
    #Модель генерации текста от Сбербанка, работает с русским, но не походит для Heroku
    #tok = AutoTokenizer.from_pretrained("sberbank-ai/rugpt3small_based_on_gpt2")
    #model = AutoModelForCausalLM.from_pretrained("sberbank-ai/rugpt3small_based_on_gpt2")

    #tok = AutoTokenizer.from_pretrained("google/t5-small-lm-adapt")
    #model = AutoModelForSeq2SeqLM.from_pretrained("google/t5-small-lm-adapt")

    #return tok.decode(model.generate(tok.encode(text, return_tensors="pt"), do_sample=True,temperature=temperature, max_length=max_length)[0])

