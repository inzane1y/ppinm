# functions_vec.py

import modules_py.functions as f
import numpy as np

k = np.r_[1e-9:5:1000j]
w = np.r_[1e-9:6:1000j]

# Auxiliary functions
w0 = np.vectorize(f.w0)

# Main functions
pi = np.vectorize(f.pi, excluded=['pf'])
pi_as = np.vectorize(f.pi_as, excluded=['pf'])

pi_delta = np.vectorize(f.pi_delta, excluded=['pf'])
pi_delta_as = np.vectorize(f.pi_delta_as, excluded=['pf'])
pi_delta_dw = np.vectorize(f.pi_delta_dw, excluded=['pf'])
pi_delta_as_dw = np.vectorize(f.pi_delta_as_dw, excluded=['pf'])

w_as = np.vectorize(f.w_as, excluded=['branch', 'pf'])

# Additional functions
s = np.vectorize(f.s, excluded=['pf', 'pi_delta_dw_part'])
s_as = np.vectorize(f.s_as, excluded=['pf', 'branch'])

gamma = np.vectorize(f.gamma, excluded=['pf'])
gamma_as = np.vectorize(f.gamma_as, excluded=['branch', 'pf'])
gamma_ff = np.vectorize(f.gamma_ff, excluded=['pf'])
gamma_ff_as = np.vectorize(f.gamma_ff_as, excluded=['branch', 'pf'])

# Convenience functions
eq0 = np.vectorize(f.eq0)
eq_pnn = np.vectorize(f.eq_pnn, excluded=['pf', 'pi_part'])
eq_pnn_as = np.vectorize(f.eq_pnn_as, excluded=['pf'])
eq_pnd = np.vectorize(f.eq_pnd, excluded=['pf', 'pi_delta_part'])
eq = np.vectorize(f.eq, excluded=['pf', 'pi_part', 'pi_delta_part'])

d0 = np.vectorize(f.d0)
d_pnn = np.vectorize(f.d_pnn, excluded=['pf', 'width', 'pi_part'])
d_pnd = np.vectorize(f.d_pnd, excluded=['pf', 'width', 'pi_delta_part'])
d = np.vectorize(f.d, excluded=['pf', 'width', 'pi_part', 'pi_delta_part'])
