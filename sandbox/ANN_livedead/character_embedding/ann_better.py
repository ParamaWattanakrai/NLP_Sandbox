import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader

# Step 1: Load data from the CSV file using NumPy
data = np.loadtxt('onehotipa.csv', delimiter=',')  # Replace 'data.csv' with the actual file path

# Step 2: Split the data into input and output
input_data = data[:, :87]
output_data = data[:, 87:]

# Step 3: Convert NumPy arrays to PyTorch tensors
input_tensor = torch.tensor(input_data, dtype=torch.float32)
output_tensor = torch.tensor(output_data, dtype=torch.float32)

# Step 4: Create datasets and dataloaders for training
dataset = TensorDataset(input_tensor, output_tensor)
dataloader = DataLoader(dataset, batch_size=64, shuffle=True)  # Adjust batch_size as needed

# Step 5: Define the neural network architecture
class SimpleANN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleANN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linearม(hidden_size, output_size)

    def forward(self, x):
        x = torch.sigmoid(self.fc1(x))
        x = self.fc2(x)
        return x

# Step 6: Define hyperparameters
input_size = 87  # Number of input features
hidden_size = 64  # Number of neurons in the hidden layer
output_size = 16  # Number of output features
learning_rate = 0.001
num_epochs = 1000

# Step 7: Create the ANN instance and set the loss function and optimizer
model = SimpleANN(input_size, hidden_size, output_size)
criterion = nn.MSELoss()  # Mean Squared Error loss for regression tasks
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Step 8: Training loop
for epoch in range(num_epochs):
    model.train()  # Set the model in training mode

    for inputs, targets in dataloader:
        # Forward pass
        outputs = model(inputs)
        loss = criterion(outputs, targets)

        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # Print training progress
    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

# Step 9: You can now use the trained model for prediction
model.eval()  # Set the model in evaluation mode
with torch.no_grad():
    test_input = torch.tensor(some_test_data, dtype=torch.float32)  # Replace some_test_data with your test data
    predictions = model(test_input)
    # Perform further processing or analysis on the predictions if needed