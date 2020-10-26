# DESCENTE DE GRADIENT
import numpy as np

def hypothesis(theta_0, theta_1, x):
	return (theta_0 + (theta_1 * x))

def predict(theta_0, theta_1, X):
    return [theta_0 + x * theta_1 for x in X]

def derivative_theta_0(theta_0, theta_1, data):
    value = sum([x[2] - x[1] for x in data])
    print("derivative_theta_0")
    print (value)
    return value

def derivative_theta_1(theta_0, theta_1, data):
    value = sum([(x[2] - x[1]) * x[0] for x in data])
    print("derivative_theta_1")
    print (value)
    return value

def cost_function(data, m):
    cost = np.sum([(x[1] - x[2]) ** 2 for x in data]) / (2 * m)
    return cost

# Tant qu'on n'a pas : une convergence, un coût à 0, ou une divergence
#       1. on calcule prev_cost
#   	2. on calcule le temp0 et temp1 simultanément
#   	3. on assigne theta_0 et theta_1
def gradient_descent(theta_0, theta_1, m, alpha, data, max_iterations):
    i = 0
    prev_cost = -1
    cost = -3
    delta = -1
    while (cost != 0 and np.abs(cost - prev_cost) > 1e-5 and i < max_iterations):
        #adding predictions in data: [x, y, h(x)]
        data = [[x[0], x[1], hypothesis(theta_0, theta_1, x[0])] for x in data]
        if (delta < 0):
            alpha /= 2
        prev_cost = cost_function(data, m)
        derivative_0 = (-2 / m) * derivative_theta_0(theta_0, theta_1, data)
        derivative_1 = (-2 / m) * derivative_theta_1(theta_0, theta_1, data)
        theta_0 = theta_0 - alpha * derivative_0
        theta_1 = theta_1 - alpha * derivative_1
        data = [[x[0], x[1], hypothesis(theta_0, theta_1, x[0])] for x in data]
        cost = cost_function(data, m)
        delta = prev_cost - cost
        i += 1
    return(theta_0, theta_1, i, cost)