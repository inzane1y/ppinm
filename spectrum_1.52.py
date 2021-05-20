import modules_py.functions as f
import modules_py.functions_vec as fv
import modules_py.proc_image as pi
import modules_py.aux as aux

import numpy as np
import matplotlib.pyplot as plt

pf = 1.52

def d_pnd_w_imag(k, w):
    return f.d_pnd(k, w, pf).imag

K, W = np.meshgrid(fv.k, fv.w)
F = d_pnd_w_imag(K, W)
_, F_lower = aux.split(K, W, F, .5, 1.4)
F_upper, _ = aux.split(K, W, F, .03, 2.1)

w_upper = np.array([])
for k_index in range(0, len(K[0, :])):
    w_index = np.argmax(F_upper[:, k_index])
    w_upper = np.append(w_upper, W[w_index, 0])

w_lower = np.array([])
for k_index in range(0, len(K[0, :])):
    w_index = np.argmax(F_lower[:, k_index])
    w_lower = np.append(w_lower, W[w_index, 0])

color_soft_pink = '#f67280'
color_dark_grey = '#363636'

plt.plot(fv.k, w_upper, label=r'max$(\Im D_{\pi N \Delta})$',
    ls='dashed', color=color_soft_pink)
plt.plot(fv.k, w_lower, ls='dashed', color=color_soft_pink)
pi.plot('graph_data_eq_pnd_real', label=r'$\omega(k)$', color=color_dark_grey)
plt.plot(fv.k, fv.w_as(fv.k, pf, branch=1), color=color_dark_grey,
    label=r'$\omega^{(as)}(k)$', ls='dotted')
plt.plot(fv.k, fv.w_as(fv.k, pf, branch=-1), color=color_dark_grey, ls='dotted')
plt.xlabel(r'$k$')
plt.ylabel(r'$\omega$')
pi.show('figures/spectrum_1.52')
