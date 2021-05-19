# proc_image.py

import matplotlib.pyplot as plt
import modules_py.proc_data as pd
import os

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

def show(filename=None):
    plt.grid()
    plt.legend()
    plt.savefig(filename + '.png', dpi=300, format='PNG') \
        if filename is not None else plt.show()
    plt.clf()

def plot(file_dir, label=None, ls=None, color=None):
    filenames = os.listdir(file_dir)
    x, Y = pd.gen_data(file_dir + '/' + filenames[0])
    main_line = plt.plot(x, Y[0], label=label, ls=ls, color=color)
    for y in Y[1:]:
        plt.plot(x, y, ls=ls, color=main_line[0].get_color())
    for filename in filenames[1:]:
        x, Y = pd.gen_data(file_dir + '/' + filename)
        for y in Y:
            plt.plot(x, y, ls=ls, color=main_line[0].get_color())

