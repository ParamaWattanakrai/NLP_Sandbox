import os
import csv
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader

character_embeddings = {}

C_PATH = os.path.dirname(__file__)
embedding_filepath = os.path.join(C_PATH, 'data/thai_character_embedding.csv')

with open(embedding_filepath, 'r', encoding='utf-8') as f:
    unstructured_character_embeddings = csv.reader(f)
    for row in unstructured_character_embeddings:
        character_embeddings[row[0]] = row[1:]

# class LivedeadDataset(Dataset):
#     def __init__(self):
#         keyvalue = np.loadtxt('LSTM_livedead/data/livedead.csv', delimiter=",", dtype=str, skiprows=1, encoding='utf-8')
#         self.key = torch.from_numpy(keyvalue[:, 1:].astype(np.float32))
#         self.label = keyvalue[:, [0]].tolist()
#         self.n_samples = keyvalue.shape[0]

#     def __getitem__(self, index):
#         key = self.key[index]
#         label = self.label[index][0]
#         return key, label

#     def __len__(self):
#         return self.n_samples

# dataset = LivedeadDataset()
# Loader  = DataLoader(dataset=dataset, batch_size=10, shuffle=False)
# dataiter = iter(Loader)
# data = next(dataiter)
# features, labels = data

# print(f'{features}\n')
# print(f'{labels}\n')
