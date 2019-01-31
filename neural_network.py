from matrix import Matrix
from math import exp

def sigmoid(x):
    return 1 / (1 + exp(-x))

def dsigmoid(y):
    return y * (1 - sigmoid(y))

class NeuralNetwork:
    def __init__(self, num_in=2, num_hid=3, num_out=1):
        self.num_input_nodes = num_in
        self.num_hidden_nodes = num_hid
        self.num_output_nodes = num_out
        self.learning_rate = 0.1
        
        self.weights_input_hidden = Matrix(self.num_hidden_nodes, self.num_input_nodes)
        self.weights_hidden_output = Matrix(self.num_output_nodes, self.num_hidden_nodes)
        
        self.weights_input_hidden.randomize()
        self.weights_hidden_output.randomize()
        
        self.bias_hidden = Matrix(self.num_hidden_nodes, 1)
        self.bias_output = Matrix(self.num_output_nodes, 1)
        
    def predict(self, input_arr, activation_func=None):
        if activation_func is None:
            activation_func = sigmoid
        inputs = Matrix.from_array(input_arr)
        #generating hidden inputs
        hidden = Matrix.multiply(self.weights_input_hidden, inputs)
        hidden.add(self.bias_hidden)
        #activation function
        hidden.apply_func(activation_func)
        
        #generating hidden output
        output = Matrix.multiply(self.weights_hidden_output, hidden)
        output.add(self.bias_output)
        output.apply_func(activation_func)
        
        return output.to_array()
    
    def train(self, inputs_arr, targets_arr, activation_func=None):
        if activation_func is None:
            activation_func = sigmoid
        inputs = Matrix.from_array(inputs_arr)
        #generating hidden inputs
        hidden = Matrix.multiply(self.weights_input_hidden, inputs)
        hidden.add(self.bias_hidden)
        #activation function
        hidden.apply_func(activation_func)
        
        #generating hidden output
        guesses = Matrix.multiply(self.weights_hidden_output, hidden)
        guesses.add(self.bias_output)
        guesses.apply_func(activation_func)
        
        targets = Matrix.from_array(targets_arr)
        
        #calculate error: error = targets - guess
        output_errors = Matrix.subtract(targets, guesses)
        #calculate gradient
        gradients = Matrix.static_apply_func(guesses, dsigmoid)
        gradients.scale(output_errors)
        gradients.scale(self.learning_rate)
        
        transposed_hidden = Matrix.static_transpose(hidden)
        weight_hidden_output_deltas = Matrix.multiply(gradients, transposed_hidden)
        
        #adjust weights by deltas
        self.weights_hidden_output.add(weight_hidden_output_deltas)
        #bias deltas are just gradients
        self.bias_output.add(gradients)
        
        #calculate the hidden layer errors -> would need a loop to make this work with more hidden layers
        transposed_weights_hidden_output = Matrix.static_transpose(self.weights_hidden_output)
        hidden_errors = Matrix.multiply(transposed_weights_hidden_output, output_errors)
        
        #calc hidden gradient
        hidden_gradient = Matrix.static_apply_func(hidden, dsigmoid)
        hidden_gradient.scale(hidden_errors)
        hidden_gradient.scale(self.learning_rate)
        
        #calc input to hidden deltas
        transposed_inputs = Matrix.static_transpose(inputs)
        weights_input_hidden_deltas = Matrix.multiply(hidden_gradient, transposed_inputs)
        
        self.weights_input_hidden.add(weights_input_hidden_deltas)
        self.bias_hidden.add(hidden_gradient)
        
    def set_learning_rate(self, n):
        self.learning_rate = n
