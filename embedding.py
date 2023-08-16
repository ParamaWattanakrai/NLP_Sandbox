import os
import csv
import torch

character_embeddings = {}

C_PATH = os.path.dirname(__file__)
embedding_filepath = os.path.join(C_PATH, 'feature/onehot68.csv')

with open(embedding_filepath, 'r', encoding='utf-8') as f:
    unstructured_character_embeddings = csv.reader(f)
    for idx, row in enumerate(unstructured_character_embeddings):
        if idx >= 1:
            character_embeddings[row[0]] = row[1:]

def embed(line):
    embedding = torch.zeros(len(line), 1, 68)
    for i, character in enumerate(line):
        character_vector = character_embeddings.get(character)
        if character_vector is not None:
            for j, dimension_value in enumerate(character_vector):
                embedding[i][0][j] = float(dimension_value)
    return embedding