# price_estimate.py

# GOAL: gets a mileage as an input, and output the estimated price based on theta_0 and tetha_1


mileage = float(input("Enter mileage: "))
theta_0 = float(input("Enter theta_0: "))
theta_1 = float(input("Enter theta_1: "))

print("price is : " + str(theta_0 + theta_1 * mileage))
print("mileage is : " + str(mileage))
print("theta_0 is : " + str(theta_0))
print("theta_1 is : " + str(theta_1))
