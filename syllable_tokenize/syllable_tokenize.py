import torch
import torch.nn as nn
import torch.optim as optim
from pythainlp.tokenize import syllable_tokenize

n_input = 16
n_hidden = 128
n_output = 2
batch_size = 1
learning_rate = 0.005
num_epochs = 30000

# class ANN(nn.Module):
#     def __init__(self, input_size, hidden_size, output_size):
#         super(ANN, self).__init__()
#         self.hidden_size = hidden_size
#         self.relu = nn.ReLU
#         self.hidden_layer = nn.Linear(input_size + hidden_size, hidden_size)
#         self.output_layer = nn.Linear(hidden_size, output_size)
#         self.softmax = nn.LogSoftmax(dim=1)
    
#     def forward(self, input):
#         hidden1 = self.relu(self.hidden_layer(input)) 
#         output = self.softmax(self.output_layer(hidden1))
#         return output 

# model = ANN(n_input, n_hidden, n_output)

# criterion = nn.NLLLoss()
# optimizer = optim.Adam(model.parameters(), lr=learning_rate)

while True:
    sentence = input("\n>>> ")
    if sentence.lower() == "ออก":
        break
    if sentence.lower() == "":
        print("ใส่คำมา")
        continue
    syllable_sentan = syllable_tokenize(sentence, keep_whitespace=False)
    TwoSyllable = []
    for i in range(len(syllable_sentan) - 1):
        TwoSyllable.append([syllable_sentan[i], syllable_sentan[i+1]])

    print(TwoSyllable)
    
