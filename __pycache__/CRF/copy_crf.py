import torch
import torch.nn as nn
import torch.optim as optim

from torchcrf import CRF

# Sample training data
X_train = [
    [('I', 'PRON'), ('love', 'VERB'), ('to', 'PREP'), ('code', 'NOUN')],
    [('ChatGPT', 'NOUN'), ('is', 'VERB'), ('awesome', 'ADJ')],
]

y_train = [
    ['PRP', 'V', 'P', 'N'],
    ['N', 'V', 'ADJ'],
]

# Create vocabulary and tagset
word_to_idx = {'<PAD>': 0, '<UNK>': 1}
tag_to_idx = {'<PAD>': 0}
for sent_tags in y_train:
    for tag in sent_tags:
        if tag not in tag_to_idx:
            tag_to_idx[tag] = len(tag_to_idx)

# Convert words and tags to indices
X_train_idx = [[word_to_idx.get(word, word_to_idx['<UNK>']) for word, _ in sent] for sent in X_train]
y_train_idx = [[tag_to_idx[tag] for tag in sent_tags] for sent_tags in y_train] 

class CRFModel(nn.Module):
    def __init__(self, num_tags, pad_idx):
        super(CRFModel, self).__init__()
        self.embedding = nn.Embedding(len(word_to_idx), 50)
        self.linear = nn.Linear(50, num_tags)  # Linear layer for emissions
        self.crf = CRF(num_tags, batch_first=True)
    
    def forward(self, x):
        x = self.embedding(x)
        emissions = self.linear(x)
        return emissions

num_tags = len(tag_to_idx)
model = CRFModel(num_tags, word_to_idx['<PAD>'])


# Loss and optimizer
criterion = model.crf
optimizer = optim.Adam(model.parameters())

# Training loop
num_epochs = 10000
for epoch in range(num_epochs):
    model.train()
    total_loss = 0
    
    for inputs, targets in zip(X_train_idx, y_train_idx):
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

input_sentence = input("Enter a sentence: ").split()

# Convert input sentence to indices
input_sentence_idx = [word_to_idx.get(word, word_to_idx['<UNK>']) for word in input_sentence]
input_tensor = torch.tensor(input_sentence_idx).unsqueeze(0)

# Put the model in evaluation mode
model.eval()

# Get emissions
with torch.no_grad():
    emissions = model(input_tensor)

# Use Viterbi algorithm to predict the best sequence of tags
with torch.no_grad():
    predicted_tags = model.crf.decode(emissions)

# Convert predicted tag indices to actual tags
predicted_tags = [list(tag_to_idx.keys())[idx] for idx in predicted_tags[0]]

print("Input Sentence:", " ".join(input_sentence))
print("Predicted Tags:", " ".join(predicted_tags))