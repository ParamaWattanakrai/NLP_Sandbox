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
output_filepath = os.path.join(C_PATH, 'embedded_dataset.csv')

with open(embedding_filepath, 'r', encoding='utf-8') as f:
    unstructured_character_embeddings = csv.reader(f)
    for row in unstructured_character_embeddings:
        character_embeddings[row[0]] = row[1:]

with open(dataset_filepath, 'r', encoding='utf-8') as f:
    unstructured_dataset = csv.reader(f)
    for row in unstructured_dataset:
        dataset_dict[row[0]] = row[1:]

for key in dataset_dict:
    embedded_sample = dataset_dict[key]
    for char in key:
        char_embedding = character_embeddings[char]
        embedded_sample = np.concatenate((embedded_sample,char_embedding))
    print(embedded_sample)
    print("sddsdssd")
    embedded_dataset.append(embedded_sample.tolist())

print(embedded_dataset)

with open(output_filepath, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(embedded_dataset)