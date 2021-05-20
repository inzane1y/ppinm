import modules_py.proc_image as pi
import matplotlib.pyplot as plt

pi.plot('graph_data_eq_pnn_real', label=r'$\omega(k)$', color='#363636')
plt.title(r'$\Re (w^2 - k^2 - 1 - \Pi_{\pi NN}) = 0$, $p_F = 1.52$')
plt.xlabel(r'$k$')
plt.ylabel(r'$\omega$')
pi.show('figures/eq_pnn_real_1.52')
