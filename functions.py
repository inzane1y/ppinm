import numpy as np

# _dx === derivative with respect to x
# _as === asymptote

M = 6.67
F_DELTA = 1.7
F = 1
W_DELTA = 2.1
LAMBDA_N = 6

# Auxiliary functions
def a(k, w):
    return w - k ** 2 / (2 * M)

def b(k, pf):
    return k * pf / M

def a_dw(w):
    return 1 # - w / M

def w_delta(k):
    return W_DELTA + k ** 2 / (2 * M)

def w0(k):
    '''Spectrum for free pion.'''
    return np.sqrt(1 + k ** 2)

def n0(pf):
    return pf ** 3 / (6 * np.pi ** 2)

# Main building blocks
def phi0(k, w, pf):
    '''Migdal's function.'''
    aa = a(k, w)
    bb = b(k, pf)
    return (M / k) ** 3 / (4 * np.pi ** 2) * ((aa ** 2 - \
        bb ** 2) / 2 * np.log(0j + (aa + bb) / (aa - bb)) - aa * bb)

def phi0_dw(k, w, pf):
    '''Migdal's function derivative.'''
    aa = a(k, w)
    bb = b(k, pf)
    return a_dw(w) * (M / k) ** 3 / (4 * np.pi ** 2) * \
        (aa * np.log(0j + (aa + bb) / (aa - bb)) - 2 * bb)

def phi0_as(k, w, pf):
    '''Asymptotic Migdal's function.'''
    return -n0(pf) / a(k, w)

def phi0_as_dw(k, w, pf):
    '''Asymptotic Migdal's function derivative.'''
    return a_dw(w) * n0(pf) / a(k, w) ** 2

# Main functions
def pi(k, w, pf):
    '''Polarization operator for pNN interaction.'''
    return -4 * F ** 2 * k ** 2 * \
        (phi0(k, w, pf) + phi0(-k, -w, pf))

def pi_as(k, w, pf):
    '''Polarization operator for pNN interaction asymptote.'''
    return -4 * F ** 2 * k ** 2 * \
        (phi0_as(k, w, pf) + phi0(-k, -w, pf))

def pi_delta(k, w, pf):
    '''Polarization operator for pND interaction.'''
    return -16 / 9 * F_DELTA ** 2 * k ** 2 * \
        (phi0(k, w - W_DELTA, pf) + phi0(-k, -w - W_DELTA, pf))

def pi_delta_as(k, w, pf):
    '''Polarization operator for pND interaction asymptote.'''
    return -16 / 9 * F_DELTA ** 2 * k ** 2 * \
        (phi0_as(k, w - W_DELTA, pf) + phi0_as(-k, -w - W_DELTA, pf))

def pi_delta_dw(k, w, pf):
    '''Polarization operator for pND interaction derivative.'''
    return -16 / 9 * F_DELTA ** 2 * k ** 2 * \
        (phi0_dw(k, w - W_DELTA, pf) + phi0_dw(-k, -w - W_DELTA, pf))

def pi_delta_as_dw(k, w, pf):
    '''Polarization operator for pND interaction asymptote derivative.'''
    return -16 / 9 * F_DELTA ** 2 * k ** 2 * \
        (phi0_as_dw(k, w - W_DELTA, pf) - phi0_as_dw(-k, -w - W_DELTA, pf))

def w_as(k, pf, branch=1):
    '''Asymptotic spectrum.'''
    w_quad_tmp = w0(k) ** 2 * w_delta(k) ** 2 - 32 / 9 * \
        F_DELTA ** 2 * n0(pf) * k ** 2 * w_delta(k)
    return np.sqrt(1 / 2 * (w_delta(k) ** 2 + w0(k) ** 2 + branch * \
        np.sqrt((w_delta(k) ** 2 + w0(k) ** 2) ** 2 - 4 * w_quad_tmp)))

# Additional functions
def gamma(k, w, pf):
    '''Gamma.'''
    return 2 * w0(k) / (2 * w - pi_delta_dw(k, w, pf))

def gamma_as(k, pf, branch=1):
    '''Gamma asymptote.'''
    w_as_tmp = w_as(k, pf, branch=branch)
    return 2 * w0(k) / (2 * w_as_tmp - pi_delta_as_dw(k, w_as_tmp, pf))

def gamma_ff(k, w, pf):
    '''Gamma with form-factor.'''
    return 2 * w0(k) / (2 * w - \
        ff_pnd(k) * pi_delta_dw(k, w, pf))

def gamma_ff_as(k, pf, branch=1):
    '''Gamma asymptote with form-factor.'''
    w_as_tmp = w_as(k, pf, branch=branch)
    return 2 * np.sqrt(1 + k **  2) / (2 * w_as_tmp - \
        ff_pnd(k) ** 2 * pi_delta_as_dw(k, w_as_tmp, pf))

def ff_pnn(k):
    '''Form-factor for pNN.'''
    return np.exp(-k ** 2 / LAMBDA_N ** 2) * 1

def ff_pnd(k):
    '''Form-factor for pND.'''
    return ff_pnn(k) / np.sqrt(1 + .23 * k ** 2)

# Convenience functions
def eq0(k, w):
    '''Equation for free pion.'''
    return w ** 2 - w0(k) ** 2

def eq_pnn(k, w, pf):
    '''Equation for pNN interaction.'''
    return eq0(k, w) - pi(k, w, pf)

def eq_pnd(k, w, pf):
    '''Equation for pND interaction.'''
    return eq0(k, w) - pi_delta(k, w, pf)

def eq(k, w, pf):
    '''Equation with all interactions.'''
    return eq0(k, w) - pi(k, w, pf) - pi_delta(k, w, pf)

def d0(k, w):
    '''Propagator for free pion.'''
    return 1 / eq0(k, w)

def d_pnn(k, w, pf, width=1e-2):
    '''Propagator for pNN interacting pion.'''
    return 1 / (eq_pnn(k, w, pf) - 1j * width)

def d_pnd(k, w, pf, width=1e-2):
    '''Propagator for pND interacting pion.'''
    return 1 / (eq_pnd(k, w, pf) - 1j * width)

def d(k, w, pf, width=1e-2):
    '''Propagator for pion in total.'''
    return 1 / (eq(k, w, pf) - 1j * width)
