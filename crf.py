import torch
import torch.nn as nn
import torch.optim as optim
from crf_segmentation import X_train, Y_train, Y_before
from torchcrf import CRF

char_to_idx = {'<UNK>': 1}
tag_to_idx = {}
for sent_tags in Y_train:
    for tag in sent_tags:
        if tag not in tag_to_idx:
            tag_to_idx[tag] = len(tag_to_idx)

X_train_idx = [[char_to_idx.get(char, char_to_idx['<UNK>']) for char in word] for word in X_train]
Y_train_idx = [[tag_to_idx[tag] for tag in word_tags] for word_tags in Y_train]

print(char_to_idx)
print(tag_to_idx)

print(X_train_idx)
print(Y_train_idx)

class CRFModel(nn.Module):
    def __init__(self, num_tags):
        super(CRFModel, self).__init__()
        self.embedding = nn.Embedding(len(char_to_idx), 50)
        self.linear = nn.Linear(50, num_tags)
        self.crf = CRF(num_tags, batch_first=True)
    
    def forward(self, x):
        x = self.embedding(x)
        emissions = self.linear(x)
        return emissions

num_tags = len(tag_to_idx)
model = CRFModel(num_tags)

criterion = model.crf
optimizer = optim.SGD(model.parameters(), lr = 0.01)

num_epochs = 1000
for epoch in range(num_epochs):
    model.train()
    total_loss = 0
    
    for inputs, targets in zip(X_train_idx, Y_train_idx):
        inputs = torch.tensor(inputs).unsqueeze(0)
        targets = torch.tensor(targets).unsqueeze(0)
        
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = -criterion(outputs, targets)
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
    
    avg_loss = total_loss / len(X_train_idx)
    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {avg_loss:.4f}")

while True:
    input_sentence = input("Enter a sentence: ").split()
    print(input_sentence)
    input_word = [(char)for char in input_sentence[0]]
    print(input_word)
    input_sentence_idx = [char_to_idx.get(word, char_to_idx['<UNK>']) for word in input_word]
    print(input_sentence_idx)
    input_tensor = torch.tensor(input_sentence_idx).unsqueeze(0)
    print(input_tensor)

    model.eval()

    with torch.no_grad():
        emissions = model(input_tensor)

    with torch.no_grad():
        predicted_tags = model.crf.decode(emissions)

    print(predicted_tags)
    predicted_tags = [list(tag_to_idx.keys())[idx] for idx in predicted_tags[0]]
    print("Input Sentence:", " ".join(input_sentence))
    print("Predicted Tags:", " ".join(predicted_tags))