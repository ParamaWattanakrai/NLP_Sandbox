import os
import csv
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader, random_split
import math

character_embeddings = {}

C_PATH = os.path.dirname(__file__)
embedding_filepath = os.path.join(C_PATH, 'data/thai_character_embedding.csv')

with open(embedding_filepath, 'r', encoding='utf-8') as f:
    unstructured_character_embeddings = csv.reader(f)
    for row in unstructured_character_embeddings:
        character_embeddings[row[0]] = row[1:]

class LivedeadDataset(Dataset):
    def __init__(self):
        keyvalue = np.loadtxt('LSTM_livedead/data/dataset.csv', delimiter=",", dtype=str, skiprows=1, encoding='utf-8')
        self.key = torch.from_numpy(keyvalue[:, 1:].astype(np.float32))
        self.label = keyvalue[:, [0]].tolist()
        self.n_samples = keyvalue.shape[0]

    def __getitem__(self, index):
        key = self.key[index]
        label = self.label[index][0]
        return key, label

    def __len__(self):
        return self.n_samples

def Dataload(dataset=LivedeadDataset(), batch_size=1, train_ratio=0.7):
    train_size = int(train_ratio * len(dataset))
    test_size = len(dataset) - train_size

    train_dataset, test_dataset = random_split(dataset, [train_size, test_size])

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    return train_loader, test_loader

    return train_loader, test_loader

def Embedding(Wordlist):
    embedding = []
    for word in Wordlist:
        Word_tensor = torch.zeros(len(word), 16)
        for i, character in enumerate(word):
            character_vector = character_embeddings.get(character)
            if character_vector is not None:
                for j, dimension_value in enumerate(character_vector):
                    Word_tensor[i][j] = float(dimension_value)
        embedding.append(Word_tensor)
    return embedding

def Getdata():
    train_data, test_data = Dataload()

    dataiter = iter(train_data)
    data = next(dataiter)
    features_train, (labels_train) = data

    dataiter = iter(test_data)
    data = next(dataiter)
    features_test, (labels_test) = data

    return features_train, labels_train, features_test, labels_test

if __name__ == '__main__':    
    features_train, labels_train, features_test, labels_test = Getdata()
    
    print(features_test)
    print(labels_test)

    print(features_train)
    print(labels_train)
