import os
import csv
import numpy as np

character_embeddings = {}
dataset_dict = {}
embedded_dataset = []
key_embedding = ""

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
    embedded_sample = np.array(dataset_dict[key], dtype=float)
    for char in key:
        char_embedding = character_embeddings[char]
        embedded_sample = np.concatenate((embedded_sample, char_embedding))
    embedded_sample = embedded_sample.reshape(-1)
    print(embedded_sample)
    print("sddsdssd")
    embedded_dataset.append(embedded_sample)
