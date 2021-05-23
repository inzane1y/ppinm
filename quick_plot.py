#! python

import modules_py.proc_image as pi
import modules_py.functions_vec as fv

from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import os

cmap_pi = ListedColormap(['#ffffff00', '#a1ae25']) # Green
cmap_pi_delta = ListedColormap(['#ffffff00', '#ec4f43']) # Red
alpha = .2

graph_data = 'graph_data'
color_dark_grey = '#363636'
dirnames = os.listdir(graph_data)

for dirname in dirnames:
    pf = dirname.split('_')[-1]
    pi.plot(graph_data + '/' + dirname,
        label=r'$\omega(k)$', color=color_dark_grey)
    plt.title(
        r'$\Re (w^2 - k^2 - 1 - \Pi_{\pi NN} - '
        r'\Pi_{\pi N \Delta}) = 0$, $p_F = ' + pf + r'$'
    )
    plt.contourf(fv.K, fv.W, fv.pi(fv.K, fv.W, float(pf)).imag > 0,
        alpha=alpha, cmap=cmap_pi)
    plt.contourf(fv.K, fv.W, fv.pi_delta(fv.K, fv.W, float(pf)).imag > 0,
        alpha=alpha, cmap=cmap_pi_delta)
    plt.xlabel(r'$k$')
    plt.ylabel(r'$\omega$')
    pi.show('figures/' + dirname)
