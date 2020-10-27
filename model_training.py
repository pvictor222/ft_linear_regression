# import sources
from src.read_data import read_data
from src.gradient_descent import gradient_descent
from src.data_visualisation import data_visualisation

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

    # Data normalisation using the maximum absolute scaling
    x_min = np.min([x for x,y in data])
    y_min = np.min([y for x,y in data])
    x_max = np.max([x for x,y in data])
    y_max = np.max([y for x,y in data])
    data_normalised = [[x / x_max, y / y_max] for x,y in data]

    # Define the maximum number of iterations
    max_iterations = input("Enter the maximum number of iterations (1000 if not specified): ")
    if (max_iterations == '' or max_iterations.isnumeric() == False):
        max_iterations = int(1000)
    else:
        max_iterations = int(max_iterations)
    print("The maximum number of iterations is: " + str(max_iterations) + "\n")

    # Gradient descent
    print("Starting the gradient descent with theta_0 = " + str(theta_0) + ", theta_1 = " + str(theta_1) + " and the learning rate = " + str(alpha) + "...")
    gradient_result = gradient_descent(theta_0, theta_1, alpha, data_normalised, max_iterations)

    # denormalize theta_0 and theta1
    theta_0 = gradient_result[0]
    theta_1 = gradient_result[1]
    theta_0 = round(theta_0 * y_max, 4)
    theta_1 = round(theta_1 * y_max / x_max, 4)

    # Printing theta_0 and theta_1
    print("\nLinear regression completed!")
    print("Theta_0 = " + str(theta_0))
    print("Theta_1 = " + str(theta_1))
    print("Hypothesis: h(x) = " + str(theta_0) + " + " + str(theta_1) + " * x")
    print("Number of iterations: " + str(gradient_result[2]))
    print ("Cost = " + str(round(gradient_result[3])))
    print ("Learning rate = " + str(gradient_result[4]))

    # Open fiLe and overwrite the content with the new theta_0 and theta_1
    theta = str(theta_0) + ';' + str(theta_1)
    f = open("theta.txt", "w")
    f.write(theta)
    f.close()

    # data visualisation
    data_visualisation(data, theta_0, theta_1)