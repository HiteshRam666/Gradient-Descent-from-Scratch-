# Gradient Descent for Linear Regression 
# yhat = wx + b
# loss = (y-yhat)**2/N

import numpy as np

# Initialize some parameters
x = np.random.randn(10, 1)
y = 2*x + np.random.rand()

# Parameters 
w = 0.0
b = 0.0
# HyperParameters
learning_rate = 0.01

print(x.shape[0])
# Create Gradient descent function 
def descend(x, y, w, b, learning_rate):
    dldw = 0.0
    dldb = 0.0
    N = x.shape[0]
    # Loss = (y - (wx+ b))**2
    for xi, yi in zip(x, y):
        dldw += -2*xi*(yi-(w*xi+b))
        dldb += -2*(yi-(w*xi+b))

    # Make an update to the w parameter
    w = w - learning_rate * (1/N)*dldw
    b = b - learning_rate * (1/N)*dldb
    return w, b


# Iteratively make updates
for epoch in range(400):
    w, b = descend(x, y, w, b, learning_rate)
    yhat = w * x  + b
    loss = np.divide(np.sum((y - yhat)**2, axis = 0), x.shape[0])
    print(f'{epoch} loss is {loss}, parameters w:{w}, b:{b}')
    # Run Gradient Descent

