#! python

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

graph_data = 'graph_data'
function_name = 'eq_pnn_real'
working_dir = graph_data + '/' + function_name
PF = os.listdir(working_dir)

function_name_i = 'eq_pnn_real_i'
working_dir_i = graph_data + '/' + function_name_i

for pf in PF:
    # Account for real solutions here
    filenames = os.listdir(working_dir + '/' + pf)
    for filename in filenames:
        integral_values = np.array([])
        K, W = pd.gen_data(working_dir + '/' + pf + '/' + filename)
        for i, k in enumerate(K):
            integral_value, _ = quad(integrand_pnn, 1e-9, np.inf, args=(k, float(pf)))
            integral_value *= 2. / np.pi
            for w in W[:, i]:
                if f.d_pnn(k, w, float(pf), width=0).imag == 0:
                    integral_value += 2 * w / (2 * w - f.pi_dw(k, w, float(pf)))
            integral_values = np.append(integral_values, integral_value)
        plt.plot(K, integral_values, color='#363636')

    # Account for imaginary solutions here
    filenames_i = os.listdir(working_dir_i + '/' + pf)
    for filename_i in filenames_i:
        integral_values_i = np.array([])
        K_i, W_i = pd.gen_data(working_dir_i + '/' + pf + '/' + filename_i)
        if np.size(W_i) == 0:
            continue
        for i, k in enumerate(K_i):
            integral_value_i = 0
            for w in W_i[:, i]:
                if f.d_pnn(k, 1j * w, float(pf), width=0).imag < 1e-4:
                    integral_value_i += (2j * w / (2j * w - (-1j) * f.pi_dw(k, 1j * w, float(pf)))).real
            integral_values_i = np.append(integral_values_i, integral_value_i)
        plt.plot(K_i, integral_values_i, color='#FFA45C')

    # plt.ylim(0, 1.3)
    plt.xlabel('$k$')
    plt.title(
        r'$\frac{2}{\pi} \int_0^\infty \omega \Im D_{\pi NN}(\omega, k) d\omega + '
        r'\sum_i \frac{2 \omega_i}{2 \omega_i - '
        r'\partial \Pi(\omega, k) / \partial \omega}$, '
        r'$p_F = ' + pf + r'$'
    )
    pi.show('figures/integral_values_' + pf)
