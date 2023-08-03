import io
import os
import glob
import csv
import torch
import random

character_embeddings = {}

C_PATH = os.path.dirname(__file__)
embedding_filepath = os.path.join(C_PATH, 'thai_character_embedding.csv')
dataTrain_filepath = os.path.join(C_PATH, 'data/train/*.csv')
dataTest_filepath = os.path.join(C_PATH, 'data/test/*.csv')

with open(embedding_filepath, 'r', encoding='utf-8') as f:
    unstructured_character_embeddings = csv.reader(f)
    for row in unstructured_character_embeddings:
        character_embeddings[row[0]] = row[1:]

def find_files(path):
    return glob.glob(path)

def read_lines(filename):
    lines = io.open(filename, encoding='utf-8').read().strip().split('\n')
    return [line for line in lines]

def load_data(directory):
    category_lines = {}
    all_categories = []
    
    for filename in find_files(directory):
        category = os.path.splitext(os.path.basename(filename))[0]
        all_categories.append(category)
        
        lines = read_lines(filename)
        category_lines[category] = lines
        
    return category_lines, all_categories

def load_data_train():
    return load_data(dataTrain_filepath)

def load_data_test():
    return load_data(dataTest_filepath)

def line_to_tensor(line):
    line_tensor = torch.zeros(len(line), 1, 16)
    for i, character in enumerate(line):
        character_vector = character_embeddings.get(character)
        if character_vector is not None:
            for j, dimension_value in enumerate(character_vector):
                line_tensor[i][0][j] = float(dimension_value)
    return line_tensor

def random_training_example(category_lines, all_categories):
    category = random.choice(all_categories)
    line = random.choice(category_lines[category])
    category_tensor = torch.tensor([all_categories.index(category)], dtype=torch.long)
    line_tensor = line_to_tensor(line)
    return category, line, category_tensor, line_tensor

def category_from_output(output, all_categories):
    category_idx = torch.argmax(output).item()
    return all_categories[category_idx]

if __name__ == '__main__':    
    category_lines_test, all_categories_test = load_data_test()
    print(line_to_tensor('เป็น').size())