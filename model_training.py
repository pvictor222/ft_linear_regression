# import sources
from src.read_data import read_data
from src.gradient_descent import gradient_descent
from src.data_visualisation import data_visualisation

# initializing variables

if __name__ == '__main__':
    theta_0 = 1
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
    max_iterations = input("Enter the maximum number of iterations (1000 if not specified): ")
    if max_iterations == '':
        max_iterations = int(1000)
    else:
        max_iterations = int(max_iterations)

    # Gradient descent
    gradient_result = gradient_descent(cost, prev_cost, theta_0, theta_1, m, alpha, data, max_iterations)

    # Printing theta_0 and theta_1
    theta_0 = round(gradient_result[0], 4)
    theta_1 = round(gradient_result[1], 4)
    print("Linear regression hypothesis: h(x) = " + str(theta_1) + " * x + " + str(theta_0))
    print("Number of iterations: " + str(gradient_result[2]))
    print ("Cost = " + str(round(gradient_result[3])))

    # open fine and overwrite the content with the new theta_0 and theta_1
    theta = str(theta_0) + ';' + str(theta_1)
    f = open("theta.txt", "w")
    f.write(theta)
    f.close()

    # data visualisation
    data_visualisation(data, theta_0, theta_1)

    # to save the variable, maybe this? ==> https://stackoverflow.com/questions/43631456/passing-a-single-variable-from-one-python-program-to-another-program
