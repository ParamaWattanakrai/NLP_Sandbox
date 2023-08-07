import torch
import time
import torch.nn as nn
from utils import loaddata, embedding, random_training, category_from_output

category_lines_train, all_categories_train, category_lines_test, all_categories_test  = loaddata()

# hyperparameter
n_input = 16
n_hidden = 128
n_categories = len(all_categories_train)
batch_size = 1
learning_rate = 0.005
num_epochs = 10000

class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size
        self.relu = nn.ReLU()

        self.hidden_layer1 = nn.Linear(input_size + hidden_size, hidden_size)
        self.hidden_layer = nn.Linear(hidden_size, hidden_size)
        self.output_layer = nn.Linear(hidden_size, output_size)
        self.softmax = nn.LogSoftmax(dim=1)
    
    def forward(self, input, hidden_state):
        combined = torch.cat((input, hidden_state), 1)
        hidden1 = self.relu(self.hidden_layer1(combined)) 
        hidden2 = self.relu(self.hidden_layer(hidden1))
        output = self.softmax(self.output_layer(hidden2))
        return output, hidden2 
    
    def init_hidden(self,batch_size):
        return torch.zeros(batch_size, self.hidden_size)

def train(line_tensor, category_tensor):
    hidden = rnn.init_hidden(batch_size)
    rnn.zero_grad()

    for i in range(line_tensor.size()[0]):
        output, hidden = rnn(line_tensor[i], hidden)

    loss = criterion(output, category_tensor)

    loss.backward()
    optimizer.step()

    return output, loss.item()

def predict(input_line):
    with torch.no_grad():
        line_tensor = embedding(input_line)
        hidden = rnn.init_hidden(batch_size)

        for i in range(line_tensor.size()[0]):
            output, hidden = rnn(line_tensor[i], hidden)

        guess = category_from_output(output, all_categories_train)
        print(f"Prediction: {guess}\n")

rnn = RNN(n_input, n_hidden, n_categories)

criterion = nn.NLLLoss()
optimizer = torch.optim.Adam(rnn.parameters(), lr=learning_rate)

current_loss = 0
print_steps = 10
correct_predictions = 0
total_predictions = 0

# ----------------------------------------- Training -----------------------------------------#

print("Start Training")
start_time = time.time()

for epoch in range(num_epochs):
    category, line, category_tensor, line_tensor = random_training(category_lines_train, all_categories_train)
    
    output, loss = train(line_tensor, category_tensor)
    current_loss += loss

    guess = category_from_output(output, all_categories_train)
    correct = "CORRECT" if guess == category else f"WRONG ({category})"

    total_predictions += 1
    if guess == category:
        correct_predictions += 1

    if (epoch + 1) % print_steps == 0:
        accuracy = correct_predictions / total_predictions
        print(f"Epoch: {epoch+1} --> {(epoch + 1) / num_epochs * 100:.2f} % Loss: {loss:.4f} Word: {line} / Guess: {guess} --> {correct} Accuracy: {accuracy:.2%}")

end_time = time.time()
training_time = end_time - start_time
accuracy = correct_predictions / total_predictions

print(f"Training time: {training_time:.2f} seconds")
print(f"Training Accuracy: {accuracy:.2%}\n")

# torch.save(rnn.state_dict(), 'trained_rnn_model.pth')
# rnn = RNN(16, n_hidden, n_categories)
# rnn.load_state_dict(torch.load('trained_rnn_model.pth'))
# rnn.eval()  

# ----------------------------------------- Testing -----------------------------------------#

start_time = time.time()

correct_predictions_test = 0
total_predictions_test = 0

print("Testing...")
laps = 0

for category in all_categories_test:
    for line in category_lines_test[category]:
        laps += 1
        category_tensor = torch.tensor([all_categories_test.index(category)], dtype=torch.long)
        line_tensor = embedding(line)

        with torch.no_grad():
            hidden = rnn.init_hidden(batch_size)

            for i in range(line_tensor.size()[0]):
                output, hidden = rnn(line_tensor[i], hidden)

            guess = category_from_output(output, all_categories_train)

        total_predictions_test += 1
        if guess == category:
            correct_predictions_test += 1

        correct = "CORRECT" if guess == category else f"WRONG ({category})"
        print(f"Lap: {laps} Input: {line} / Predicted: {guess} --> {correct}")

end_time = time.time()
training_time = end_time - start_time
test_accuracy = correct_predictions_test / total_predictions_test

print(f"Testing time: {training_time:.2f} seconds")
print(f"Test Accuracy: {test_accuracy:.2%}")

print("\nสรุปผลบ")
print(f"Training Accuracy: {accuracy:.2%}")
print(f"Test Accuracy: {test_accuracy:.2%}")

while True:
    sentence = input("\n>>> ")
    if sentence.lower() == "ออก":
        break
    if sentence.lower() == "":
        print("ใส่คำมาสิไอเปรต")
        continue

    predict(sentence)

print("Exiting.")