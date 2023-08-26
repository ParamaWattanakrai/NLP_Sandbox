import os
import csv
import torch
import random

character_embeddings = {}
dataset_dict = {}

C_PATH = os.path.dirname(__file__)
embedding_filepath = os.path.join(C_PATH, 'data/onehot68_copy.csv')
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

def Loaddata(train_proportion=0.75):
    total_samples = len(dataset_dict)
    num_samples = int(train_proportion * total_samples)
    random_keys = list(dataset_dict.keys())
    random.shuffle(random_keys)

    train_data = {key: dataset_dict[key] for key in random_keys[:num_samples]}
    test_data = {key: dataset_dict[key] for key in random_keys[num_samples:]}
    
    category_lines_train = {value[0]: [] for values in train_data.values() for value in values}
    for key, values in train_data.items():
        for value in values:
            category_lines_train[value[0]].append(key)

    category_lines_test = {value[0]: [] for values in test_data.values() for value in values}
    for key, values in test_data.items():
        for value in values:
            category_lines_test[value[0]].append(key)

    all_categories_train = list(category_lines_train.keys())
    all_categories_test = list(category_lines_test.keys())

    return category_lines_train, all_categories_train, category_lines_test, all_categories_test

def Embedding(line):
    embedding = torch.zeros(len(line), 1, 68)
    for i, character in enumerate(line):
        character_vector = character_embeddings.get(character)
        if character_vector is not None:
            for j, dimension_value in enumerate(character_vector):
                embedding[i][0][j] = float(dimension_value)
    return embedding

def Random_training(category_lines, all_categories):
    category = random.choice(all_categories)
    line = random.choice(category_lines[category])
    category_tensor = torch.tensor([all_categories.index(category)], dtype=torch.long)
    line_tensor = Embedding(line)
    return category, line, category_tensor, line_tensor

def Category_from_output(output, all_categories):
    category_idx = torch.argmax(output).item()
    return all_categories[category_idx]
