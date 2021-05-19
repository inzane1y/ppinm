import numpy as np

def gen_data(filename):
    data = np.genfromtxt(filename);
    return data[:, 0], data[:, 1:].transpose()
