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
    
    def propagate_backward(self, error, lr=0.1):
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
        self.weight = data["weight"]
        self.bias = data["bias"]

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

ins = np.array([[0.42,0.5,0.12,1,0.5,0.4,0.6,0.3,1,0.2]])
target = np.array([0,1])

layerone = linear(10,12)
layertwo = linear(12,2)
for s in range(100):
    x = relu(layerone.propagate_forward(ins))
    x = softmax(layertwo.propagate_forward(x))

    error = x - target 

    layertwo.propagate_backward(error)
    y = layertwo.find_derivative(error) *  relu(layerone.propagate_forward(ins),True)
    layerone.propagate_backward(y)

    print(error)

print(x)
layerone.save_weights("layerone")
layertwo.save_weights("layertwo")