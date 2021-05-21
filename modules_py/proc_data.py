import numpy as np
import os

def gen_data(filename):
    data = np.genfromtxt(filename);
    return data[:, 0], data[:, 1:].transpose()

# def gen_data_folder(dir_name):
#     x = np.array([])
#     for filename in os.listdir():
#         x_tmp, y_tmp = gen_data(dir_name + '/' + filename)
#         x = np.append(x, x_tmp)
