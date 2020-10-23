# import sources
from src.read_data import read_data
from src.gradient_descent import gradient_descent
from src.data_visualisation import data_visualisation

# initializing variables
theta_0 = 0
theta_1 = 0
prev_cost = -1
cost = -3
alpha = 1

# Read the data from "data.csv", remove first row and calculate m
data = read_data("data.csv")
data.pop(0)
#mileages to delete?
mileages = [[1, x[0]] for x in data]
m = len(data)

# Gradient descent
gradient_result = gradient_descent(cost, prev_cost, theta_0, theta_1, m, alpha, data)
print(gradient_result)
# Printing theta_0 and theta_1
theta_0 = round(gradient_result[0], 4)
theta_1 = round(gradient_result[1], 4)
print ("theta_0 = " + str(theta_0))
print ("theta_1 = " + str(theta_1))

# data visualisation
data_visualisation(data, theta_0, theta_1)