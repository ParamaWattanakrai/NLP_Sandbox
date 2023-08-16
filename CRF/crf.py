import torch
import torch.nn as nn
from torchcrf import CRF

# Define the character-level NER model
class CharNERModel(nn.Module):
    def __init__(self, num_chars, num_tags, char_embedding_dim, hidden_dim):
        super(CharNERModel, self).__init__()
        self.char_embedding = nn.Embedding(num_chars, char_embedding_dim)
        self.lstm = nn.LSTM(char_embedding_dim, hidden_dim, batch_first=True, bidirectional=True)
        self.hidden2tag = nn.Linear(2 * hidden_dim, num_tags)
        self.crf = CRF(num_tags)
    
    def forward(self, char_ids):
        char_embeds = self.char_embedding(char_ids)
        lstm_out, _ = self.lstm(char_embeds)
        tag_space = self.hidden2tag(lstm_out)
        return tag_space

# Dummy data
num_chars = 26  # Number of characters in the English alphabet
num_tags = 3   # Number of NER tags (B, I, O)
char_embedding_dim = 10
hidden_dim = 20

# Create the model
model = CharNERModel(num_chars, num_tags, char_embedding_dim, hidden_dim)

# Input data
manual_input_text = "i hate my life"
manual_tags = torch.tensor([0, 0, 0, 0, 1, 2, 1, 2, 1, 2, 1])  # B, I, I, I, O, B, O, B, O, B, O

# Convert characters to numerical IDs
char_sequence = [ord(c) - ord('a') for c in manual_input_text if 'a' <= c <= 'z']

# Convert the char_sequence to a PyTorch tensor
char_sequence_tensor = torch.tensor(char_sequence).unsqueeze(0)  # Add a batch dimension

# Forward pass
tag_scores = model(char_sequence_tensor)

# Create a CRF layer
crf = CRF(num_tags)

# Compute the CRF loss
crf_loss = crf(tag_scores, manual_tags.unsqueeze(0))

# Compute the log likelihood of the given tags
log_likelihood = crf.forward(tag_scores, manual_tags.unsqueeze(0))

# Decode the best sequence of tags using Viterbi algorithm
best_tags = crf.decode(tag_scores)

print("Input Text:", manual_input_text)
print("Manual Tags:", manual_tags.tolist())
print("Predicted Tags:", best_tags[0])
print("CRF Loss:", crf_loss.item())
print("Log Likelihood:", log_likelihood.item())
