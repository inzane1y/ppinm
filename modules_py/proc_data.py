import numpy as np

def gen_data(filename):
    data = np.genfromtxt(filename);
    if np.size(data) != np.shape(data)[0]:
        return data[:, 0], data[:, 1:].transpose()
    else:
        return data, np.array([])
