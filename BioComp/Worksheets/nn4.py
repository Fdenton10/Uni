import numpy as np

np.random.seed(0)

X = [[1.0, 2.0, 3.0, 2.5],
     [2.0, 5.0, -1.0, 2.0],
     [-1.5, 2.7, 3.3, -0.8]]

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

layer1 = Layer_Dense(4,5)
layer2 = Layer_Dense(5,3)

layer1.forward(X)
#print(layer1.output)
layer2.forward(layer1.output)
print(layer1.weights)

'''
Batches
Helps with generilization
Transpose = Swap rows and columns
'''
'''
layer_outputs = [] #Output of current layer
for neuron_weights, neuron_bias in zip(weights,biases):
    neuron_output = 0 #Output of given neuron
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input*weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)

print(layer_outputs)
'''

