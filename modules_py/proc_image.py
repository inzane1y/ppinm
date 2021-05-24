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

def plot(file_dir, label=None, ls=None, color='#363636'):
    flag_label_present = False
    filenames = os.listdir(file_dir)
    for filename in filenames:
        x, Y = pd.gen_data(file_dir + '/' + filename)
        for y in Y:
            if flag_label_present:
                plt.plot(x, y, ls=ls, color=color)
            else:
                plt.plot(x, y, ls=ls, color=color, label=label)
