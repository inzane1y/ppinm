# functions_vec.py

import modules_py.functions as f
import numpy as np

k = np.r_[1e-9:5:1000j]
w = np.r_[1e-9:8:1000j]

K, W = np.meshgrid(k, w)

# Auxiliary functions
w0 = np.vectorize(f.w0)

# Main functions
pi_pnn = np.vectorize(f.pi_pnn, excluded=['pf'])
pi_pnn_as = np.vectorize(f.pi_pnn_as, excluded=['pf'])

pi_pnd = np.vectorize(f.pi_pnd, excluded=['pf'])
pi_pnd_as = np.vectorize(f.pi_pnd_as, excluded=['pf'])
pi_pnd_dw = np.vectorize(f.pi_pnd_dw, excluded=['pf'])
pi_pnd_as_dw = np.vectorize(f.pi_pnd_as_dw, excluded=['pf'])

pi_pnn_corr = np.vectorize(f.pi_pnn_corr, excluded=['pf'])
pi_pnn_corr_pnd_as = np.vectorize(f.pi_pnn_corr_pnd_as, excluded=['pf'])
pi_pnn_corr_pnd = np.vectorize(f.pi_pnn_corr_pnd, excluded=['pf'])

w_as = np.vectorize(f.w_as, excluded=['branch', 'pf'])

# Additional functions
s = np.vectorize(f.s, excluded=['pf', 'pi_pnd_dw_part'])
s_as = np.vectorize(f.s_as, excluded=['pf', 'branch'])

gamma = np.vectorize(f.gamma, excluded=['pf'])
gamma_as = np.vectorize(f.gamma_as, excluded=['branch', 'pf'])
gamma_ff = np.vectorize(f.gamma_ff, excluded=['pf'])
gamma_ff_as = np.vectorize(f.gamma_ff_as, excluded=['branch', 'pf'])

# Convenience functions
eq0 = np.vectorize(f.eq0)
eq_pnn = np.vectorize(f.eq_pnn, excluded=['pf', 'pi_pnn_part'])
eq_pnn_as = np.vectorize(f.eq_pnn_as, excluded=['pf'])
eq_pnd = np.vectorize(f.eq_pnd, excluded=['pf', 'pi_pnd_part'])
eq_pnn_pnd = np.vectorize(f.eq_pnn_pnd, excluded=['pf', 'pi_pnn_part', 'pi_pnd_part'])

d0 = np.vectorize(f.d0)
d_pnn = np.vectorize(f.d_pnn, excluded=['pf', 'width', 'pi_pnn_part'])
d_pnd = np.vectorize(f.d_pnd, excluded=['pf', 'width', 'pi_pnd_part'])
d_pnn_corr_pnd = np.vectorize(f.d_pnn_corr_pnd, excluded=['pf', 'width', 'part'])
d = np.vectorize(f.d, excluded=['pf', 'width', 'pi_pnn_part', 'pi_pnd_part'])
