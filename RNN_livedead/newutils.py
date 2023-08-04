import os
import csv
import numpy as np

import torch

from torch.utils.data import Dataset, DataLoader

character_embeddings = {}
dataset_dict = {}

C_PATH = os.path.dirname(__file__)
embedding_filepath = os.path.join(C_PATH, 'thai_character_embedding.csv')
dataset_filepath = os.path.join(C_PATH, 'data/livedead.csv')

with open(embedding_filepath, 'r', encoding='utf-8') as f:
    unstructured_character_embeddings = csv.reader(f)
    for row in unstructured_character_embeddings:
        character_embeddings[row[0]] = row[1:]

with open(dataset_filepath, 'r', encoding='utf-8') as f:
    unstructured_dataset = csv.reader(f)
    for row in unstructured_dataset:
        dataset_dict[row[0]] = row[1:]



class LivedeadDataset(Dataset):

    def __init__(self):
        keyvalue = np.loadtxt('RNN_livedead/data/livedead.csv', delimiter=",", dtype=str, skiprows=1)
        self.key = torch.from_numpy(keyvalue[:, 1:])
        self.value = torch.from_numpy(keyvalue[:, [0]])
        self.n_samples = keyvalue.shape[0]

    def __getitem__(self, index):
        return self.key[index], self.value[index]

    def __len__(self):
        return self.n_samples