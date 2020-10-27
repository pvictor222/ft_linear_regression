# import sources
from src.read_data import read_data
from src.gradient_descent import gradient_descent
from src.data_visualisation import data_visualisation
from src.normalization import normalize, un_normalize

# import libraries
import random
import numpy as np

if __name__ == '__main__':
    # initializing variables
    theta_0 = 0
    theta_1 = 0
    alpha = 1
    # Read the data from "data.csv", remove first row and calculate m
    data = read_data("data.csv")
    data.pop(0)
    data = [[int(x),int(y)] for [x, y] in data]

    # Data normalisation
    x_min = np.min([x for x,y in data])
    y_min = np.min([y for x,y in data])
    x_max = np.max([x for x,y in data])
    y_max = np.max([y for x,y in data])
    data_normalised = [[normalize(x, x_min, x_max), normalize(y, y_min, y_max)] for x,y in data]
    print(data_normalised)

    max_iterations = input("Enter the maximum number of iterations (1000 if not specified): ")
    if (max_iterations == '' or max_iterations.isnumeric() == False):
        max_iterations = int(1000)
    else:
        max_iterations = int(max_iterations)

    # Gradient descent
    gradient_result = gradient_descent(theta_0, theta_1, alpha, data_normalised, max_iterations)

    # Printing theta_0 and theta_1
    theta_0 = un_normalize(round(gradient_result[0], 4), x_min, x_max)
    theta_1 = un_normalize(round(gradient_result[1], 4), x_min, x_max)
    print("Linear regression hypothesis: h(x) = " + str(theta_1) + " * x + " + str(theta_0))
    print("Number of iterations: " + str(gradient_result[2]))
    print ("Cost = " + str(round(gradient_result[3])))
    print ("Alpha = " + str(gradient_result[4]))

    # open fine and overwrite the content with the new theta_0 and theta_1
    theta = str(theta_0) + ';' + str(theta_1)
    f = open("theta.txt", "w")
    f.write(theta)
    f.close()

    # data visualisation
    data_visualisation(data_normalised, theta_0, theta_1)