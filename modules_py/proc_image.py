# proc_image.py

import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

def show(filename=None):
    plt.grid()
    plt.legend()
    plt.savefig(filename + '.png', dpi=300, format='PNG') \
        if filename is not None else plt.show()
    plt.clf()
