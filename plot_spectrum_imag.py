import modules_py.proc_image as pi
import modules_py.proc_data as pd
import modules_py.functions_vec as fv

import matplotlib.pyplot as plt
import os

pf = '3.000'

func_name = 'eq_pnn_corr'
dir_name = 'graph_data/' + func_name
pi.plot_2(dir_name, pf, fv.pi_corr, label_r=r'$\omega(k)^2$', label_i=r'$\omega(k)^2 < 0$')

# Asymptote
# func_name = 'eq_pnd_as_real'
# dir_name = 'graph_data/' + func_name
# pi.plot_2(dir_name, pf, label_r=r'$\omega(k)^2$', label_i=r'$\omega(k)^2 < 0$')

pi.contourf_imag(fv.K, fv.W, fv.pi_corr, float(pf), cmap=pi.cmap_pi_pnn_corr)

pi.gen_title(func_name, pf)
plt.xlabel(r'$k$')
plt.ylabel(r'$\omega^2$')
# plt.ylim(-1, 15)
pi.show()#'figures/' + func_name + '_r_i_' + pf)
