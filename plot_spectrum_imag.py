# pnd <=> (0, 15) for all
# pnn <=> (-.5, 15), (-.05, .05) for scale, (-1, 15) for 2.190
# pnn_corr <=> (-2, 12), (-.5, 1) for scale

import modules_py.proc_image as pi
import modules_py.functions_vec as fv

import matplotlib.pyplot as plt

# pf = '1.520' # (1.520) (1.910) (2.190)
pf = '1.910' # (1.520) (1.910) (2.190)
# pf = '2.190' # (1.520) (1.910) (2.190)

# Asymptote
# func_name = 'eq_pnn_as'
# dir_name = 'graph_data/' + func_name
# pi.plot_2_as(dir_name, pf,
#     label_r=r'$\omega^{(as)}(k)^2$',
#     label_i=r'$\omega^{(as)}(k)^2 < 0$')

func_name = 'eq_pnn_corr_pnd'
dir_name = 'graph_data/' + func_name
pi.plot_2(dir_name, pf, fv.pi_pnn_corr_pnd,
    label_r=r'$\omega(k)^2$',
    label_i=r'$\omega(k)^2 < 0$')

# plt.plot([0, .002501], [0, .0006799375 ** 2], color=pi.color_black) # Connect with zero
# plt.plot([0, .002501], [0, .0006799375 ** 2], color=pi.color_black) # Connect with zero

pi.gen_title(func_name, pf)
pi.contourf_imag(fv.K, fv.W, fv.pi_pnn_corr, float(pf), cmap=pi.cmap_pi_pnn_corr)
pi.contourf_imag(fv.K, fv.W, fv.pi_pnd, float(pf), cmap=pi.cmap_pi_pnd)

plt.xlabel(r'$k$')
plt.ylabel(r'$\omega^2$')
# plt.ylim(0, 15)
# plt.xlim(0, .4)
pi.show('figures/' + func_name + '_' + pf, png=True) # <<==
