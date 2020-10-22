# model_training.py

from model_training_src.read_data import read_data

# GOAL: find theta and beta

theta_0 = 0
theta_1 = 0
prev_cost = -1
cost = -3
alpha = 1

# Read the data from "data.csv"

data = read_data("data.csv")
data.pop(0)
mileages = [[1, x[0]] for x in data]
m = len(data)

# i à supprimer, slt pour tests
i = 0

# DESCENTE DE GRADIENT
# Tant qu'on n'a pas : une convergence, un coût à 0, ou une divergence
#       1. on calcule prev_cost
#   	2. on calcule le temp0 et temp1 simultanément
#   	3. on assigne theta_0 et theta_1
while (cost != 0 and cost != prev_cost and abs(cost - prev_cost) > 1):
    i += 1
    prev_cost = (sum([pow((theta_0 + theta_1 * int(x[0])) - int(x[1]), 2) for x in data]) / 2) / m
    temp0 = theta_0 - alpha * (sum([theta_0 + theta_1 * int(x[0]) - int(x[1]) for x in data]) / m)
    temp1 = theta_1 - alpha * (sum([(theta_0 + theta_1 * int(x[0]) - int(x[1])) * int(x[0]) for x in data]) / m)
    print (temp0, temp1)
    cost = (sum([pow((temp0 + temp1 * int(x[0])) - int(x[1]), 2) for x in data]) / 2) / m
    if (cost < prev_cost):
        theta_0 = temp0
        theta_1 = temp1
    else:
        alpha /= 2
    print(prev_cost, cost)
    print(theta_0, theta_1)
    print(i)
