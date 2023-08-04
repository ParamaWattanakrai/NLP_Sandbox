import os
import csv
import numpy as np

character_embeddings = {}
dataset_dict = {}
embedded_dataset_dict = {}

C_PATH = os.path.dirname(__file__)
embedding_filepath = os.path.join(C_PATH, 'thai_character_embedding.csv')
dataset_filepath = os.path.join(C_PATH, 'data/livedead.csv')

with open(embedding_filepath, 'r', encoding='utf-8') as f:
    unstructured_character_embeddings = csv.reader(f)
    for row in unstructured_character_embeddings:
        character_embeddings[row[0]] = row[1:]

with open(dataset_filepath, 'r', encoding='utf-8') as f:
    unstructured_dataset = csv.reader(f)
    for row in unstructured_dataset:
        dataset_dict[row[0]] = row[1:]

for key in dataset_dict:
    key_embedding = []    
    for char in key:
        char_embedding = character_embeddings[char]
        key_embedding.append(char_embedding)
    key_embedding

print(char_embedding)