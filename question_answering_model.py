import os
import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline, set_seed

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

def generate_text(text, max_length, num_return_sequences):
    generator = pipeline('text-generation', model='gpt2')
    set_seed(42)
    
    return generator(text, max_length=max_length, num_return_sequences=num_return_sequences))
