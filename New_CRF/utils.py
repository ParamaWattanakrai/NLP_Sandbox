import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np

class Data():
    def __init__(self, label, one_hot, ipa, vector):
        self.label = label
        self.one_hot = one_hot
        self.ipa = ipa
        self.vector = vector
    
    def getInformation(self):
        return f'Label: {self.label}\nOne Hot: {self.one_hot}\nIPA: {self.ipa}\nVector: {self.vector}'
    def getVector(self):
        return self.vector


class DataLoader():
    def __init__(self):
        character_embedded = np.genfromtxt('New_CRF/data/character_embedded.csv', delimiter=",", dtype='str', skip_header=1, encoding='utf-8')
        data_vectors = np.genfromtxt('New_CRF/data/data_vectors.csv', delimiter=",", dtype='str', encoding='utf-8')

        self.label = character_embedded[:, 0]
        self.one_hot = torch.from_numpy(character_embedded[:, 2:70].astype(np.float32))
        self.ipa = torch.from_numpy(character_embedded[:, 70:86].astype(np.float32))
        self.vector = torch.from_numpy(data_vectors[:, 1:].astype(np.float32))
        self.list_of_data = []
        for index, char in enumerate(self.label):
            self.list_of_data.append(Data(self.label[index], self.one_hot[index], self.ipa[index], self.vector[index]))
    
    def searchData(self, label):
        target_label = label

        selected_data = None
        for data in self.list_of_data:
            if data.label == target_label:
                selected_data = data
                return selected_data

        if selected_data is None:
            return f'No object found with label: {target_label}'

if __name__ == '__main__':
    data = DataLoader()

    while True:
        sentence = input("\n>>> ")
        for char in sentence: 
            print(char)
            print(data.searchData(char).getVector())
