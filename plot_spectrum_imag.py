import modules_py.proc_image as pi
import modules_py.proc_data as pd
import modules_py.functions_vec as fv

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

import numpy as np
import os

color_red = '#F62A66'
color_black = '#363636'

pf = '2.700'
func_name = 'eq_real'

r_filenames = os.listdir('graph_data/' + func_name + '/' + pf)
i_filenames = os.listdir('graph_data/' + func_name + '_i/' + pf)

r_label_done = False
for r_filename in r_filenames:
    k, W = pd.gen_data('graph_data/' + func_name + '/' + pf + '/' + r_filename)
    for w in W:
        if not r_label_done:
            plt.plot(k, w ** 2, label=r'$\omega(k)^2$', color=color_black)
            r_label_done = True
        else:
            plt.plot(k, w ** 2, color=color_black)

for i_filename in i_filenames:
    k, W = pd.gen_data('graph_data/' + func_name + '_i/' + pf + '/' + i_filename)
    for w in W:
        plt.plot(k, -w ** 2, color=color_red)

# Asymptote
# func_name = 'eq_pnd_as_real'
# r_filenames = os.listdir('graph_data/' + func_name + '/' + pf)
# i_filenames = os.listdir('graph_data/' + func_name + '_i/' + pf)

# r_label_done = False
# for r_filename in r_filenames:
#     k, W = pd.gen_data('graph_data/' + func_name + '/' + pf + '/' + r_filename)
#     for w in W:
#         if not r_label_done:
#             plt.plot(k, w ** 2, label=r'$\omega^{(as)}(k)^2$', color=color_black, ls='dotted')
#             r_label_done = True
#         else:
#             plt.plot(k, w ** 2, color=color_black, ls='dotted')

# for i_filename in i_filenames:
#     k, W = pd.gen_data('graph_data/' + func_name + '_i/' + pf + '/' + i_filename)
#     for w in W:
#         plt.plot(k, -w ** 2, color=color_red, ls='dotted')


cmap_pi = ListedColormap(['#ffffff00', '#a1ae25']) # Green
cmap_pi_delta = ListedColormap(['#ffffff00', '#ec4f43']) # Red
plt.contourf(fv.K, fv.W * fv.W,
    np.abs(fv.pi_delta(fv.K, fv.W, float(pf)).imag) > 1e-5,
    alpha=.2, cmap=cmap_pi_delta)

plt.contourf(fv.K, fv.W * fv.W,
    np.abs(fv.pi(fv.K, fv.W, float(pf)).imag) > 1e-5,
    alpha=.2, cmap=cmap_pi)

# plt.contourf(fv.K, -fv.W * fv.W,
#     np.abs(fv.pi(fv.K, 1j * fv.W, float(pf)).imag) > 1e-5,
#     alpha=.2, cmap=cmap_pi)

plt.title(r'$\pi N N + \pi N \Delta$')
plt.xlabel(r'$k$')
plt.ylabel(r'$\omega^2$')
plt.ylim(-5, 15)
pi.show('figures/' + func_name + '_both_r_i_' + pf)
