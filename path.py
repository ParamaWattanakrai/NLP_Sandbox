import os
import csv

import numpy as np

character_embeddings = {}

C_PATH = os.path.dirname(__file__)
embedding_filepath = os.path.join(C_PATH, 'character_embeddings.csv')

with open(embedding_filepath, 'r') as f:
    unstructured_character_embeddings = csv.reader(f)
    for row in unstructured_character_embeddings:
        character_embeddings[row[0]] = row[1:]

def format_input(word):
    formatted_input = np.zeros((1,696))
    matrix_index = 0
    for character in word:
        character_vector = character_embeddings[character]
        for dimension_value in character_vector:
            formatted_input[0][matrix_index] = dimension_value
            matrix_index += 1
    return formatted_input

ins = format_input('เคราะห์')
print(ins)