import io
import os
import glob
import csv
import torch
import random

character_embeddings = {}
dataset_dict = {}

C_PATH = os.path.dirname(__file__)
embedding_filepath = os.path.join(C_PATH, 'thai_character_embedding.csv')

with open(embedding_filepath, 'r', encoding='utf-8') as f:
    unstructured_character_embeddings = csv.reader(f)
    for row in unstructured_character_embeddings:
        character_embeddings[row[0]] = row[1:]

def load_data_train():
    category_lines_train = {}
    all_categories_train = []
    
    def find_files(path):
        return glob.glob(path)
    
    def read_lines(filename):
        lines = io.open(filename, encoding='utf-8').read().strip().split('\n')
        return [line for line in lines]
    
    for filename in find_files('Data/train/*.csv'):
        category = os.path.splitext(os.path.basename(filename))[0]
        all_categories_train.append(category)
        
        lines = read_lines(filename)
        category_lines_train[category] = lines
        
    return category_lines_train, all_categories_train

def load_data_test():
    category_lines_test = {}
    all_categories_test = []
    
    def find_files(path):
        return glob.glob(path)
    
    def read_lines(filename):
        lines = io.open(filename, encoding='utf-8').read().strip().split('\n')
        return [line for line in lines]
    
    for filename in find_files('Data/test/*.csv'):
        category = os.path.splitext(os.path.basename(filename))[0]
        all_categories_test.append(category)
        
        lines = read_lines(filename)
        category_lines_test[category] = lines
        
    return category_lines_test, all_categories_test

def letter_to_tensor(word):
    letter_tensor = torch.zeros((1, 16))
    matrix_index = 0
    for character in word:
        character_vector = character_embeddings[character]
        for dimension_value in character_vector:
            letter_tensor[0][matrix_index] = float(dimension_value)  #
            matrix_index += 1
    return letter_tensor

def line_to_tensor(line):
    line_tensor = torch.zeros(len(line), 1, 16)
    for i, character in enumerate(line):
        character_vector = character_embeddings.get(character)
        if character_vector is not None:
            for j, dimension_value in enumerate(character_vector):
                line_tensor[i][0][j] = float(dimension_value)
    return line_tensor

def random_training_example(category_lines, all_categories):
    
    def random_choice(a):
        random_idx = random.randint(0, len(a) - 1)
        return a[random_idx]
    
    category = random_choice(all_categories)
    line = random_choice(category_lines[category])
    category_tensor = torch.tensor([all_categories.index(category)], dtype=torch.long)
    line_tensor = line_to_tensor(line)
    return category, line, category_tensor, line_tensor

def category_from_output(output, all_categories):
    category_idx = torch.argmax(output).item()
    return all_categories[category_idx]

if __name__ == '__main__':    
    category_lines_test, all_categories_test = load_data_test()
    print(category_lines_test['live'][:5])

    print(letter_to_tensor('ก'))
    print(line_to_tensor('การ').size())