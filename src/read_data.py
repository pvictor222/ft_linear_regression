# GET THE DATA FROM data.csv

def read_data(csv):
    f = open(csv, "r")
    temp = f.read().split()
    data = [x.split(',') for x in temp]
    return (data)