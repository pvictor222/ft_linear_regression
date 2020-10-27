# DESCENTE DE GRADIENT
import numpy as np

def hypothesis(theta_0, theta_1, x):
    return (theta_0 + (theta_1 * x))

def cost_function(theta_0, theta_1, data):
    cost = 0
    for x,y in data:
        cost += (y - hypothesis(theta_0, theta_1, x))**2
    return cost/len(data)

# Repeat until the cost function converges or the maximum number of iterations is met
#       1. Calculate the previous cost (before)
#   	2. Update theta_0 and theta_1 simultaneously
#   	3. Calculate the new cost (after) and the delta between before and after
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