import os.path
from os import path

# GOAL: gets a mileage as an input, and output the estimated price based on theta_0 and tetha_1
if __name__ == '__main__':
    if path.exists("theta.txt"):
        f = open("theta.txt", "r")
        temp = f.read().split(";")
        theta_0 = float(temp[0])
        theta_1 = float(temp[1])
    else:
        theta_0 = 0
        theta_1 = 0

    mileage = input("Enter mileage (0 if undefined): ")
    if (mileage == '' or mileage.isnumeric() == False):
        mileage = int(0)
    else:
        mileage = int(mileage)

    # The price cannot be negative
    print("The estimated price for a car with a mileage of " + str(mileage) + "km is : " + str(max(round(theta_0 + theta_1 * mileage), 0)) + "$")
