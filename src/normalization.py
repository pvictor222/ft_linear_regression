# normalization

def normalize(x, x_min, x_max):
    return (x - x_min) / (x_max - x_min)

def un_normalize(x, x_min, x_max):
    return x * (x_max - x_min) + x_min