import os
import csv

import os
import csv

import random
import numpy as np

np.random.seed(428)

character_embeddings = {}
dataset_dict = {}

C_PATH = os.path.dirname(__file__)
embedding_filepath = os.path.join(C_PATH, 'character_embeddings.csv')
dataset_filepath = os.path.join(C_PATH, 'livedead.csv')

with open(embedding_filepath, 'r', encoding='utf-8') as f:
    unstructured_character_embeddings = csv.reader(f)
    for row in unstructured_character_embeddings:
        character_embeddings[row[0]] = row[1:]

with open(dataset_filepath, 'r', encoding='utf-8') as f:
    unstructured_dataset = csv.reader(f)
    for row in unstructured_dataset:
        dataset_dict[row[0]] = row[1:]

print(dataset_dict)
keys_list = list(dataset_dict.keys())
print(keys_list)
random.shuffle(keys_list)
print(keys_list)