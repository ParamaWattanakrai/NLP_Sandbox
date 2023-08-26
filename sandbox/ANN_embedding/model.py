from utils import DataLoader
import torch
import torch.nn as nn
import csv

data_loader = DataLoader()

input_size = 68
hidden_size = 2
output_size = 16

model = nn.Sequential(
    nn.Linear(input_size, hidden_size),
    nn.Linear(hidden_size, output_size),
    nn.Sigmoid()
)

mseLoss = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

def weight_reset(model):
    if isinstance(model, nn.Linear):
        model.reset_parameters()

csv_data = []

for epoch in range(10000):
    for index, data_instance in enumerate(data_loader.list_of_data):
        model.apply(weight_reset)
        input_layer = data_instance.one_hot.view(1, -1)
        output_layer = data_instance.ipa.view(1, -1)
        predicted = model(input_layer)
        loss = mseLoss(predicted, output_layer)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
    if (epoch+1) % 1 == 0:
        print(f'epoch: {epoch + 1}, loss = {loss.item():.5f}')
    
    data_instance.vector = model[0].weight[:, index]


    csv_data.append([data_instance.label] + data_instance.vector.tolist())

csv_file = 'sandbox/ANN_embedding\data_vectors.csv'
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)