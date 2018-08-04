def add_metrices(x,y):
    return [[x[a][b] + y[a][b] for b in range(len(x[0]))] for a in range(len(x))]

def sub_metrices(x,y):
    return [[x[a][b] - y[a][b] for b in range(len(x[0]))] for a in range(len(x))]

