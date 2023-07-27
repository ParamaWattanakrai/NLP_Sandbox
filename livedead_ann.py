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
        if len(row[0]) != 3:
            continue
        dataset_dict[row[0]] = row[1:]

class linear:
    def __init__(self, previous_nodes, next_nodes):
        self.previous_nodes = previous_nodes
        self.weights = np.random.randn(previous_nodes, next_nodes)
        self.biases = np.zeros((1, next_nodes))
    
    def propagate_forward(self, previous_activations):
        self.previous_activations = previous_activations
        product = np.matmul(previous_activations, self.weights)
        output = product + self.biases
        return output
    
    def propagate_backward(self, error, learning_rate=0.1):
        derivative_of_weights = np.matmul(self.previous_activations.T, error)
        derivative_of_biases = np.sum(error, axis=0)
        self.weights -= derivative_of_weights * learning_rate
        self.biases -= derivative_of_biases * learning_rate
    
    def find_derivative(self, error):
        d = np.dot(error, self.weights.T)
        return d
    
    def save_weights(self, filename):
        np.savez(filename, weights=self.weights, biases=self.biases)
    
    def load_weights(self, filename):
        data = np.load(filename)
        self.weights = data["weights"]
        self.biases = data["biases"]

def softmax(x, derivative=False):
    if not derivative:
        exp_x = np.exp(x)
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)
    else:
        return softmax(x) * (1 - softmax(x).sum(axis=1, keepdims=True))

def relu(x,derivative = False):
    if not derivative:
        return np.maximum(0, x)
    else:
        return (x > 0).astype(float)

def format_input(word):
    formatted_input = np.zeros((1,696))
    matrix_index = 0
    for character in word:
        character_vector = character_embeddings[character]
        for dimension_value in character_vector:
            formatted_input[0][matrix_index] = dimension_value
            matrix_index += 1
    return formatted_input

def train(training_input, training_target, iteration):

    for current_iteration in range(iteration):
        activation_one = relu(layerone.propagate_forward(training_input))
        activation_two = softmax(layertwo.propagate_forward(activation_one))

        error = activation_two - training_target

        layertwo.propagate_backward(error)
        second_backpropagation_value = layertwo.find_derivative(error) *  relu(layerone.propagate_forward(training_input),True)
        layerone.propagate_backward(second_backpropagation_value)

        return error

def complete_forward(input_vector):
    activation_one = relu(layerone.propagate_forward(input_vector))
    activation_two = softmax(layertwo.propagate_forward(activation_one))
    return activation_two

def kfold_train(training_input, training_target, folds, iteration):
    split_input = np.array_split(training_input, folds, axis=0)
    split_target = np.array_split(training_target, folds, axis=0)

    print(train(split_input[0], split_target[0], 1))

    for k in range(folds):
        train(split_input[k], split_target[k], iteration)

    # for k in range(folds):
    #     training_set_input = np.delete(split_input, k, axis=0)
    #     training_set_target = np.delete(split_output, k, axis=0)
    #     train(training_set_input, training_set_target, iteration)

layerone = linear(696,5)
layertwo = linear(5,2)

training_input = np.zeros((1,696))
training_target = np.zeros((1,2))

shuffled_dataset_keys = list(dataset_dict.keys())
random.shuffle(shuffled_dataset_keys)

for input_key in shuffled_dataset_keys:

    formatted_input = format_input(input_key)
    formatted_target = np.zeros((1,2))

    if dataset_dict[input_key][0] == '0':
        formatted_target[0][1] = 1.
    elif dataset_dict[input_key][0] == '1':
        formatted_target[0][0] = 1.
    else:
        print("Something's wrong")

    training_input = np.concatenate((training_input, formatted_input), axis=0)
    training_target = np.concatenate((training_target, formatted_target), axis=0)
training_input = np.delete(training_input, 0, axis=0)
training_target = np.delete(training_target, 0, axis=0)

print(kfold_train(training_input, training_target, 57, 5))

print(complete_forward(format_input('ลัก')))