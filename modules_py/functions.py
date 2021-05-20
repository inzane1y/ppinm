# functions.py

import numpy as np
import modules_py.proc_part as p

# _dx === derivative with respect to x
# _as === asymptote

# Parameters
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
        (phi0_dw(k, w - W_DELTA, pf) - phi0_dw(-k, -w - W_DELTA, pf))

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
def s(k, w, pf, pi_delta_dw_part=p.P_DFLT):
    '''One term of S(k).'''
    pi_delta_dw_tmp = p.part(pi_delta_dw, pi_delta_dw_part, k, w, pf)
    return 2 * w / (2 * w - pi_delta_dw_tmp)

def s_as(k, pf, branch=1):
    '''One term of S(k) asymptotic.'''
    w_as_tmp = w_as(k, pf, branch=branch)
    return 2 * w_as_tmp / (2 * w_as_tmp - pi_delta_as_dw(k, w_as_tmp, pf))

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

def eq_pnn(k, w, pf, pi_part=p.P_DFLT):
    '''Equation for pNN interaction.'''
    pi_tmp = p.part(pi, pi_part, k, w, pf)
    return eq0(k, w) - pi_tmp

def eq_pnd(k, w, pf, pi_delta_part=p.P_DFLT):
    '''Equation for pND interaction.'''
    pi_delta_tmp = p.part(pi_delta, pi_delta_part, k, w, pf)
    return eq0(k, w) - pi_delta_tmp

def eq(k, w, pf, pi_part=p.P_DFLT, pi_delta_part=p.P_DFLT):
    '''Equation with all interactions.'''
    pi_tmp = p.part(pi, pi_part, k, w, pf)
    pi_delta_tmp = p.part(pi_delta, pi_delta_part, k, w, pf)
    return eq0(k, w) - pi_tmp - pi_delta_tmp

def d0(k, w):
    '''Propagator for free pion.'''
    return 1 / eq0(k, w)

def d_pnn(k, w, pf, width=1e-2, pi_part=p.P_DFLT):
    '''Propagator for pNN interacting pion.'''
    return 1 / (eq_pnn(k, w, pf, pi_part=pi_part) - 1j * width)

def d_pnd(k, w, pf, width=1e-2, pi_delta_part=p.P_DFLT):
    '''Propagator for pND interacting pion.'''
    return 1 / (eq_pnd(k, w, pf, pi_delta_part=pi_delta_part) - 1j * width)

def d(k, w, pf, width=1e-2, pi_part=p.P_DFLT, pi_delta_part=p.P_DFLT):
    '''Propagator for pion in total.'''
    return 1 / (eq(k, w, pf, pi_part=pi_part, pi_delta_part=pi_delta_part) - 1j * width)
