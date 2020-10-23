# import graphic libraries. Instal it with :
#    python3 -m pip install -U pip
#    python3 -m pip install -U matplotlib
import matplotlib.pyplot as plt

# DATA VISUALISATION
def data_visualisation(data, theta_0, theta_1):
    #    plotting the data
    X = [int(x[0]) for x in data]
    Y = [int(x[1]) for x in data]
    plt.scatter(X,Y, color='red')
    plt.title('Graphic representation', color='blue')
    plt.xlabel('Mileage', color='blue')
    plt.ylabel('Price', color='blue')
    plt.axis([min(X), max(X), min(Y), max(Y)])
    #   plotting the axis
    #       calculating the min and max value with our hypothesis
    x1 = min(X)
    x2 = max(X)
    y1 = theta_0 + x1 * theta_1
    y2 = theta_0 + x2 * theta_1
    x_values = [x1, x2]
    y_values = [y1, y2]
    #       inserting it in the graph
    plt.plot(x_values, y_values, color='pink')
    #   display the graph
    plt.show()