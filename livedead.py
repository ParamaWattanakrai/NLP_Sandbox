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
    
    def propagate_backward(self, error, lr=0.1):
        dw = np.matmul(self.previous_activations.T, error)
        db = np.sum(error, axis=0)
        self.weights -= dw * lr
        self.biases -= db * lr
    
    def find_derivative(self, error):
        d = np.dot(error, self.weights.T)
        return d
    
    def save_weights(self, filename):
        np.savez(filename, weights=self.weights, biases=self.biases)
    
    def load_weights(self, filename):
        data = np.load(filename)
        self.weight = data["weight"]
        self.bias = data["bias"]

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

def train(iteration):
    

    for current_iteration in range(iteration):
        activation_one = relu(layerone.propagate_forward(training_input))
        activation_two = softmax(layertwo.propagate_forward(x))

        error = activation_two - target

        layertwo.propagate_backward(error)
        second_backpropagation_value = layertwo.find_derivative(error) *  relu(layerone.propagate_forward(training_input),True)
        layerone.propagate_backward(y)

        return error

print()