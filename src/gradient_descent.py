# DESCENTE DE GRADIENT

def hypothesis(theta_0, theta_1, x):
	return (theta_0 + (theta_1 * x))

def sum_theta_0(theta_0, theta_1, data, m):
    value = 0
    for i in (0, m - 1):
        value += hypothesis(theta_0, theta_1, int(data[i][0])) - int(data[i][1])
    return value

def sum_theta_1(theta_0, theta_1, data, m):
    value = 0
    for i in (0, m - 1):
        value += (hypothesis(theta_0, theta_1, int(data[i][0])) - int(data[i][1])) * int(data[i][0])
    return value

# Tant qu'on n'a pas : une convergence, un coût à 0, ou une divergence
#       1. on calcule prev_cost
#   	2. on calcule le temp0 et temp1 simultanément
#   	3. on assigne theta_0 et theta_1
def gradient_descent(cost, prev_cost, theta_0, theta_1, m, alpha, data, max_iterations):
    i = 0
    while (cost != 0 and abs(cost - prev_cost) > 1e-5 and i < max_iterations ):
        prev_cost = sum([pow(theta_0 + (theta_1 * int(x[0])) - int(x[1]), 2) for x in data]) / (2 * m)
        temp0 = theta_0 - ((alpha / m) * sum_theta_0(theta_0, theta_1, data, m))
        temp1 = theta_1 - ((alpha / m) * sum_theta_1(theta_0, theta_1, data, m))
        cost = sum([pow(temp0 + (temp1 * int(x[0])) - int(x[1]), 2) for x in data]) / (2 * m)
        if (cost < prev_cost):
            theta_0 = temp0
            theta_1 = temp1
        else:
            alpha /= 2
        i += 1
    print(round(theta_0, 6))
    print(round(theta_1, 6))
    return(theta_0, theta_1, i, cost)