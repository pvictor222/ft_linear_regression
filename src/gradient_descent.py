# DESCENTE DE GRADIENT
import numpy as np

# def predict(theta_0, theta_1, X):
#     return [theta_0 + x * theta_1 for x in X]

# def derivative_theta_0(theta_0, theta_1, data):
#     value = sum([x[2] - x[1] for x in data])
#     print("derivative_theta_0")
#     print (value)
#     return value

# def derivative_theta_1(theta_0, theta_1, data):
#     value = sum([(x[2] - x[1]) * x[0] for x in data])
#     print("derivative_theta_1")
#     print (value)
#     return value

def hypothesis(theta_0, theta_1, x):
    return (theta_0 + (theta_1 * x))

def cost_function(theta_0, theta_1, data):
    cost = 0
    for x,y in data:
        cost += (y - hypothesis(theta_0, theta_1, x))**2
    return cost/len(data)

# Tant qu'on n'a pas : une convergence, un coût à 0, ou une divergence
#       1. on calcule prev_cost
#   	2. on calcule le temp0 et temp1 simultanément
#   	3. on assigne theta_0 et theta_1
def gradient_descent(theta_0, theta_1, alpha, data, max_iterations):
    i = 0
    delta = float('inf')
    while (np.abs(delta) > 1e-5 and i < max_iterations):
        i += 1
        before = cost_function(theta_0, theta_1, data)
        derivative_0 = -2 * np.sum([y - hypothesis(theta_0, theta_1, x) for x,y in data]) / len(data)
        derivative_1 = -2 * np.sum([(y - hypothesis(theta_0, theta_1, x)) * x for x,y in data]) / len(data)
        theta_0 -= alpha * derivative_0
        theta_1 -= alpha * derivative_1
        after = cost_function(theta_0, theta_1, data)
        delta = before - after
        if (delta < 0):
            alpha /= 2
    return(theta_0, theta_1, i, after, alpha)