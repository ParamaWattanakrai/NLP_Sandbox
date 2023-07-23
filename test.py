import numpy as np

class linear:
    def __init__(self, previous_nodes, next_nodes):
        self.previous_nodes = previous_nodes
        self.weights = np.random.randn(previous_nodes, next_nodes)
        self.biases = np.zeros((1, next_nodes))
    
    def propagate_forward(self, previous_activations):
        self.previous_activations = previous_activations
        product = np.matmul(previous_activations, self.weights)
        output = product + self.biases
        return output
    
    def propagate_backward(self, error, lr=1):
        dw = np.matmul(self.previous_activations.T, error)
        db = np.sum(error, axis=0)
        self.weights -= dw * lr
        self.biases -= db * lr
    
    def find_derivative(self, error):
        d = np.dot(error, self.weights.T)
        return d
    
    def save_weights(self, filename):
        np.savez(filename, weights=self.weights, biases=self.biases)
    
    def load_weights(self, filename):
        data = np.load(filename)
        self.weights = data["weights"]
        self.biases = data["biases"]

def softmax(x, derivative=False):
    if not derivative:
        exp_x = np.exp(x)
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)
    else:
        return softmax(x) * (1 - softmax(x).sum(axis=1, keepdims=True))

def relu(x,derivative = False):
    if not derivative:
        return np.maximum(0, x)
    else:
        return (x > 0).astype(float)

ins = np.array([[0.1,1,1]])
target = np.array([0,0,1])

layerone = linear(3,5)
layertwo = linear(5,3)

layerone.load_weights("layerone.npz")
layertwo.load_weights("layertwo.npz")

x = relu(layerone.propagate_forward(ins))
x = softmax(layertwo.propagate_forward(x))

print(x)
