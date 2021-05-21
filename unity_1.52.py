# unity_1.52.py

import modules_py.proc_image as pi
import modules_py.functions as f
import modules_py.proc_data as pd

import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.integrate import quad

def integrand_pnn(w, k, pf):
    return w * f.d_pnn(k, w, pf, width=0).imag

dir_name = 'graph_data_eq_pnn_real'
filenames = os.listdir(dir_name)
PF = [0.89, 1.52, 1.91, 2.19, 2.41]
for pf in PF:
    for filename in filenames:
        integral_values = np.array([])
        K, W = pd.gen_data(dir_name + '/' + filename)
        for i, k in enumerate(K):
            integral_value, _ = quad(integrand_pnn, 1e-9, 100, args=(k, pf))
            for w in W[:, i]:
                if f.d_pnn(k, w, pf, width=0).imag == 0:
                    integral_value += 2 * w / (2 * w - f.pi_dw(k, w, pf))
            integral_values = np.append(integral_values, integral_value)
        plt.plot(K, integral_values, color='#363636')
    plt.xlabel('$k$')
    plt.title(
        r'$\int_0^\infty \omega \Im D_{\pi NN}(\omega, k) d\omega + '
        r'\sum_i \frac{2 \omega_i}{2 \omega_i - '
        r'\partial \Pi(\omega, k) / \partial \omega}$, '
        r'$p_F = ' + str(pf) + r'$'
    )
    pi.show('figures/integral_values_' + str(pf))
