import os
import csv
import torch
import random

character_embeddings = {}
dataset_dict = {}

C_PATH = os.path.dirname(__file__)
embedding_filepath = os.path.join(C_PATH, 'data/data_vectors100000x68re.csv')
dataset_filepath = os.path.join(C_PATH, 'data/dataset.csv')

with open(embedding_filepath, 'r', encoding='utf-8') as f:
    unstructured_character_embeddings = csv.reader(f)
    for idx, row in enumerate(unstructured_character_embeddings):
        if idx >= 1:
            character_embeddings[row[0]] = row[1:]

with open(dataset_filepath, 'r', encoding='utf-8') as f:
    unstructured_dataset = csv.reader(f)
    for idx, row in enumerate(unstructured_dataset):
        if idx >= 1:
            dataset_dict[row[0]] = row[1:]

def embedding(line):
    embedding = torch.zeros(len(line), 1, 68)
    for i, character in enumerate(line):
        character_vector = character_embeddings.get(character)
        if character_vector is not None:
            for j, dimension_value in enumerate(character_vector):
                embedding[i][0][j] = float(dimension_value)
    return embedding