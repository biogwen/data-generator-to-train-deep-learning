import numpy as np
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
x, y = make_regression(n_samples=1000, n_features=1, noise=10)

plt.scatter(x, y)

y = y.reshape(y.shape[0], 1)

X = np.hstack((x, np.ones(x.shape)))

theta = np.random.randn(2, 1)
theta

def model(X, theta):
    return X.dot(theta)

plt.plot(model(X, theta))

def cost_fontion(x, y, theta):
    m = len(y)
    return 1/(2*m) * np.sum((model(X, theta) - y)**2)

cost_fontion(X, y, theta)

def grad(x, y, theta):
    m = len(y)
    return 1/m * X.T.dot(model(X, theta) - y)

def gradient_descent (X, y, theta, learning_rate, n_iterations):
    cost_history = np.zeros(n_iterations)
    for i in range(0, n_iterations):
        theta = theta - learning_rate *grad(X, y, theta)
        cost_history[i] = cost_fontion(X, y, theta)

    return theta, cost_history

theta_final, cost_history = gradient_descent(X, y, theta, learning_rate = 0.001, n_iterations=1000)

predictions = model(X, theta_final)
plt.scatter(x, y)
plt.plot(x, predictions, c='r')

plt.plot(range(1000), cost_history)

def coef(y, pred):
    u = ((y - pred)**2).sum()
    v = ((y - y.mean())**2).sum()
    return 1 - u/v

coef(y, predictions)