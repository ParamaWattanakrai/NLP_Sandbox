import torch
import time
import torch.nn as nn
import matplotlib.pyplot as plt
from utils import load_data, line_to_tensor, random_training_example, category_from_output
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size
        self.in2hidden = nn.Linear(input_size + hidden_size, hidden_size)
        self.in2output = nn.Linear(input_size + hidden_size, output_size)
        self.softmax = nn.LogSoftmax(dim=1)
    
    def forward(self, input, hidden_state):
        combined = torch.cat((input, hidden_state), 1)
        hidden = torch.relu(self.in2hidden(combined))
        output = self.softmax(self.in2output(combined))
        return output, hidden
    
    def init_hidden(self):
        return torch.zeros(1, self.hidden_size)

# Load the data
category_lines, all_categories = load_data()
n_categories = len(all_categories)
n_hidden = 128

# Initialize RNN
rnn = RNN(87, n_hidden, n_categories)
rnn.to(device)

# Training function
def train(line_tensor, category_tensor):
    hidden = rnn.init_hidden()
    rnn.zero_grad()

    for i in range(line_tensor.size()[0]):
        output, hidden = rnn(line_tensor[i], hidden)

    loss = criterion(output, category_tensor)

    loss.backward()
    optimizer.step()

    return output, loss.item()

# Initialize the loss function and optimizer
criterion = nn.NLLLoss()
learning_rate = 0.005
optimizer = torch.optim.SGD(rnn.parameters(), lr=learning_rate)
current_loss = 0
all_losses = []

print_steps = 500 
num_epochs = 10000 # ขี้เกียจ Train นานเลยปรับแค่นี้

correct_predictions = 0
total_predictions = 0

# Training loop
start_time = time.time()

for epoch in range(num_epochs):

    category, line, category_tensor, line_tensor = random_training_example(category_lines, all_categories)
    
    output, loss = train(line_tensor, category_tensor)
    current_loss += loss

    guess = category_from_output(output, all_categories)
    correct = "CORRECT" if guess == category else f"WRONG ({category})"

    total_predictions += 1
    if guess == category:
        correct_predictions += 1

    if (epoch + 1) % print_steps == 0:
        accuracy = correct_predictions / total_predictions
        print(f"{(epoch + 1) / num_epochs * 100:.2f}% Loss: {loss:.4f} Word: {line} / Guess: {guess} --> {correct} Accuracy: {accuracy:.2%}")

end_time = time.time()
training_time = end_time - start_time
accuracy = correct_predictions / total_predictions
print(f"Training time: {training_time:.2f} seconds")
print(f"Overall accuracy: {accuracy:.2%}")

# Prediction function
def predict(input_line):
    with torch.no_grad():
        line_tensor = line_to_tensor(input_line)
        hidden = rnn.init_hidden()

        for i in range(line_tensor.size()[0]):
            output, hidden = rnn(line_tensor[i], hidden)

        guess = category_from_output(output, all_categories)
        print(f"Prediction: {guess}\n")

while True:
    sentence = input(">>> ")
    if sentence.lower() == "ออก":
        break

    predict(sentence)

print("Exiting.")