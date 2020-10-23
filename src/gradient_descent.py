# DESCENTE DE GRADIENT
# Tant qu'on n'a pas : une convergence, un coût à 0, ou une divergence
#       1. on calcule prev_cost
#   	2. on calcule le temp0 et temp1 simultanément
#   	3. on assigne theta_0 et theta_1

def gradient_descent(cost, prev_cost, theta_0, theta_1, m, alpha, data):
    while (cost != 0 and abs(cost - prev_cost) > 1):
        prev_cost = sum([pow((theta_0 + (theta_1 * int(x[0]))) - int(x[1]), 2) for x in data]) / (2 * m)
        temp0 = theta_0 - ((alpha / m) * sum([theta_0 + (theta_1 * int(x[0])) - int(x[1]) for x in data]))
        temp1 = theta_1 - ((alpha / m) * sum([(theta_0 + (theta_1 * int(x[0])) - int(x[1])) * int(x[0]) for x in data]))
        cost = sum([pow((temp0 + (temp1 * int(x[0]))) - int(x[1]), 2) for x in data]) / (2 * m)
        if (cost < prev_cost):
            theta_0 = temp0
            theta_1 = temp1
        else:
            alpha /= 2
        print ("temp0 = " + str(temp0))
        print ("theta_0 = " + str(theta_0))
        print ("theta_1 = " + str(theta_1))
        print ("cost = " + str(cost))
    return(theta_0, theta_1)