# functions.py

import numpy as np
import modules_py.proc_part as p

# _dx === derivative with respect to x
# _as === asymptote

# Parameters
M = 6.67 * 0.9
F_DELTA = 1.7
F = 1
W_DELTA = 2.1
LAMBDA = 6.0
P0 = 1.88
G_MINUS = 1.6
G_DELTA = 0.8

def n(pf):
    return 2 * pf * pf * pf / (3 * np.pi * np.pi * 0.45)

# Auxiliary functions
def a(k, w):
    return w - k ** 2 / (2 * M)

def a_new(k, w):
    return w + k * k / (2.0 * M)

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

def phi1_corr(k, w, pf):
    '''Migdal's function for correlations.'''
    aa = a(k, w)
    bb = b(k, pf)

    return M ** 2 / (2 * k ** 3 * pf) * ((aa ** 2 - \
        bb ** 2) / 2. * np.log(0.j + (aa + bb) / (aa - bb)) - aa * bb)

def phi1_pnd_corr(k, w, pf):
    aa = a_new(k, w);
    bb = b(k, pf);

    return -M * M / (2.0 * k * k * k * pf) * ((aa * aa - bb * bb) /
        2.0 * np.log(0.0j  + (aa + bb) / (aa - bb)) - aa * bb);

def phi1_corr_dw(k, w, pf):
    '''Migdal's function for correlations derivative.'''
    aa = a(k, w)
    bb = b(k, pf)
    
    return M ** 2 / (2 * k ** 3 * pf) * \
        (aa * np.log(0j + (aa + bb) / (aa - bb)) - 2 * bb)

def phi1_pnd_corr_dw(k, w, pf):
    '''Migdal's function for pND correlations derivative.'''
    aa = a_new(k, w)
    bb = b(k, pf)
    
    return -M ** 2 / (2 * k ** 3 * pf) * \
        (aa * np.log(0j + (aa + bb) / (aa - bb)) - 2 * bb)

def phi_corr(k, w, pf):
    '''Lindhard's function for correlations.'''
    return phi1_corr(k, w, pf) + phi1_corr(-k, -w, pf)

def phi_corr_dw(k, w, pf):
    '''Lindhard's function for correlations derivative.'''
    return phi1_corr_dw(k, w, pf) - phi1_corr_dw(-k, -w, pf)

def phi_pnd_corr(k, w, pf):
    return phi1_pnd_corr(k, -w + W_DELTA, pf) + phi1_pnd_corr(-k, w + W_DELTA, pf);

def phi_pnd_corr_dw(k, w, pf):
    return -phi1_pnd_corr_dw(k, -w + W_DELTA, pf) + phi1_pnd_corr_dw(-k, w + W_DELTA, pf);

def a_delta(k, w, pf):
    return M * pf / (np.pi * np.pi * (1.0 + 0.23 * k * k)) * \
        phi_pnd_corr(k, w, pf);

def a_delta_dw(k, w, pf):
    return M * pf / (np.pi * np.pi * (1.0 + 0.23 * k * k)) * \
        phi_pnd_corr_dw(k, w, pf);

# Main functions
def pi_pnn(k, w, pf):
    '''Polarization operator for pNN interaction.'''
    return -4 * F ** 2 * k ** 2 * \
        (phi0(k, w, pf) + phi0(-k, -w, pf))

def pi_pnn_as(k, w, pf):
    '''Polarization operator for pNN interaction asymptote.'''
    return -4 * F ** 2 * k ** 2 * \
        (phi0_as(k, w, pf) + phi0_as(-k, -w, pf))

def pi_pnn_dw(k, w, pf):
    '''Polarization operator for pNN interaction derivative.'''
    return -4 * F ** 2 * k ** 2 * \
        (phi0_dw(k, w, pf) - phi0_dw(-k, -w, pf))

def pi_pnd(k, w, pf):
    '''Polarization operator for pND interaction.'''
    return -16 / 9 * F_DELTA ** 2 * k ** 2 * \
        (phi0(k, w - W_DELTA, pf) + phi0(-k, -w - W_DELTA, pf)) # / \
        # (1 + 0.23 * k ** 2)

def pi_pnd_as(k, w, pf):
    '''Polarization operator for pND interaction asymptote.'''
    return -16 / 9 * F_DELTA ** 2 * k ** 2 * \
        (phi0_as(k, w - W_DELTA, pf) + phi0_as(-k, -w - W_DELTA, pf))

def pi_pnd_dw(k, w, pf):
    '''Polarization operator for pND interaction derivative.'''
    return -16 / 9 * F_DELTA ** 2 * k ** 2 * \
        (phi0_dw(k, w - W_DELTA, pf) - phi0_dw(-k, -w - W_DELTA, pf)) # / \
        # (1 + 0.23 * k ** 2)

def pi_pnd_as_dw(k, w, pf):
    '''Polarization operator for pND interaction asymptote derivative.'''
    return -16 / 9 * F_DELTA ** 2 * k ** 2 * \
        (phi0_as_dw(k, w - W_DELTA, pf) - phi0_as_dw(-k, -w - W_DELTA, pf))

def pi_pnn_corr(k, w, pf):
    '''Polarization operator for pNN correlation interaction.'''
    return -2 * M * pf / (np.pi ** 2) * F ** 2 * k ** 2 * \
        phi_corr(k, w, pf) / (1 + G_MINUS * pf / P0 * phi_corr(k, w, pf))

def pi_pnn_corr_ff(k, w, pf):
    '''Polarization operator for pNN correlation interaction.'''
    return -2 * M * pf / (np.pi ** 2) * F ** 2 * k ** 2 * \
        phi_corr(k, w, pf) / (1 + G_MINUS * pf / P0 * phi_corr(k, w, pf)) * \
        np.exp(-2 * k ** 2 / LAMBDA ** 2)

def pi_pnn_corr_dw(k, w, pf):
    return -2 * M * pf / (np.pi ** 2) * F ** 2 * k ** 2 * \
        phi_corr_dw(k, w, pf) / (1 + G_MINUS * pf / P0 * phi_corr(k, w, pf)) ** 2

def pi_pnn_corr_ff_dw(k, w, pf):
    return -2 * M * pf / (np.pi ** 2) * F ** 2 * k ** 2 * \
        phi_corr_dw(k, w, pf) / (1 + G_MINUS * pf / P0 * phi_corr(k, w, pf)) ** 2 * \
        np.exp(-2 * k ** 2 / LAMBDA ** 2)

def pi_pnn_corr_pnd_as(k, w, pf):
    '''Polarization operator for pNN correlation and pND asymptote interactions.'''
    return pi_pnn_corr(k, w, pf) + pi_pnd_as(k, w, pf)

def pi_pnn_corr_pnd(k, w, pf):
    '''Polarization operator for pNN correlation and pND interactions.'''
    return pi_pnn_corr(k, w, pf) + pi_pnd(k, w, pf)

def pi_pnn_corr_pnd_dw(k, w, pf):
    return pi_pnn_corr_dw(k, w, pf) + pi_pnd_dw(k, w, pf)

def pi_pnd_corr(k, w, pf):
    return -64.0 / 25.0 * F * F * k * k * a_delta(k, w, pf) / \
        (1.0 + G_DELTA * phi_pnd_corr(k, w, pf))

def pi_pnd_corr_ff(k, w, pf):
    return -64.0 / 25.0 * F * F * k * k * a_delta(k, w, pf) / \
        (1.0 + np.exp(-2 * k ** 2 / LAMBDA ** 2) * G_DELTA * pf / P0 * phi_pnd_corr(k, w, pf)) * \
        np.exp(-2 * k ** 2 / LAMBDA ** 2)

def pi_pnd_corr_ff_dw(k, w, pf):
    return -64.0 / 25.0 * F * F * k * k * M * pf / (np.pi * np.pi * (1.0 + 0.23 * k * k)) * \
        phi_pnd_corr_dw(k, w, pf) / (1 + np.exp(-2 * k ** 2 / LAMBDA ** 2) * \
        G_DELTA * pf / P0 * phi_pnd_corr(k, w, pf)) ** 2 * \
        np.exp(-2 * k ** 2 / LAMBDA ** 2)

def pi_pnd_corr_dw(k, w, pf):
    return -64.0 / 25.0 * F * F * k * k * M * pf / (np.pi * np.pi * (1.0 + 0.23 * k * k)) * \
        phi_pnd_corr_dw(k, w, pf) / (1 + G_DELTA * pf / P0 * phi_pnd_corr(k, w, pf)) ** 2

def pi_pnn_corr_pnd_corr(k, w, pf):
    return pi_pnn_corr(k, w, pf) + pi_pnd_corr(k, w, pf)

def pi_pnn_corr_pnd_corr_dw(k, w, pf):
    return pi_pnn_corr_dw(k, w, pf) + pi_pnd_corr_dw(k, w, pf)

def pi_pnn_corr_ff_pnd_corr_ff_dw(k, w, pf):
    return pi_pnn_corr_ff_dw(k, w, pf) + pi_pnd_corr_ff_dw(k, w, pf)

def w_as(k, pf, branch=1):
    '''Asymptotic spectrum.'''
    w_quad_tmp = w0(k) ** 2 * w_delta(k) ** 2 - 32 / 9 * \
        F_DELTA ** 2 * n0(pf) * k ** 2 * w_delta(k)
    return np.sqrt(1 / 2 * (w_delta(k) ** 2 + w0(k) ** 2 + branch * \
        np.sqrt((w_delta(k) ** 2 + w0(k) ** 2) ** 2 - 4 * w_quad_tmp)))

# Additional functions
def s(k, w, pf, pi_pnd_dw_part=p.P_DFLT):
    '''One term of S(k).'''
    pi_pnd_dw_tmp = p.part(pi_pnd_dw, pi_pnd_dw_part, k, w, pf)
    return 2 * w / (2 * w - pi_pnd_dw_tmp)

def s_as(k, pf, branch=1):
    '''One term of S(k) asymptotic.'''
    w_as_tmp = w_as(k, pf, branch=branch)
    return 2 * w_as_tmp / (2 * w_as_tmp - pi_pnd_as_dw(k, w_as_tmp, pf))

def gamma(k, w, pf):
    '''Gamma.'''
    return 2 * w0(k) / (2 * w - pi_pnd_dw(k, w, pf))

def gamma_as(k, pf, branch=1):
    '''Gamma asymptote.'''
    w_as_tmp = w_as(k, pf, branch=branch)
    return 2 * w0(k) / (2 * w_as_tmp - pi_pnd_as_dw(k, w_as_tmp, pf))

def gamma_ff(k, w, pf):
    '''Gamma with form-factor.'''
    return 2 * w0(k) / (2 * w - \
        ff_pnd(k) * pi_pnd_dw(k, w, pf))

def gamma_ff_as(k, pf, branch=1):
    '''Gamma asymptote with form-factor.'''
    w_as_tmp = w_as(k, pf, branch=branch)
    return 2 * np.sqrt(1 + k **  2) / (2 * w_as_tmp - \
        ff_pnd(k) ** 2 * pi_pnd_as_dw(k, w_as_tmp, pf))

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

def eq_pnn(k, w, pf, pi_pnn_part=p.P_DFLT):
    '''Equation for pNN interaction.'''
    pi_pnn_tmp = p.part(pi_pnn, pi_pnn_part, k, w, pf)
    eq0_tmp = p.part(eq0, pi_pnn_part, k, w)
    return eq0_tmp - pi_pnn_tmp

def eq_pnn_as(k, w, pf):
    '''Equation for pNN interaction asymptote.'''
    return eq0(k, w) - pi_pnn_as(k, w, pf)

def eq_pnd(k, w, pf, pi_pnd_part=p.P_DFLT):
    '''Equation for pND interaction.'''
    pi_pnd_tmp = p.part(pi_pnd, pi_pnd_part, k, w, pf)
    return eq0(k, w) - pi_pnd(k, w, pf)

def eq_pnn_pnd(k, w, pf, part=p.P_DFLT):
    '''Equation with all interactions.'''
    pi_pnn_tmp = p.part(pi_pnn, part, k, w, pf)
    pi_pnd_tmp = p.part(pi_pnd, part, k, w, pf)
    return eq0(k, w) - pi_pnn_tmp - pi_pnd_tmp

def eq_pnn_corr(k, w, pf, part=p.P_DFLT):
    pi_pnn_corr_tmp = p.part(pi_pnn_corr, part, k, w, pf)
    eq0_tmp = p.part(eq0, part, k, w)
    # return eq0_tmp - pi_pnn_corr_tmp
    return eq0(k, w) - pi_pnn_corr(k, w, pf)

def eq_pnn_corr_pnd(k, w, pf, part=p.P_DFLT):
    eq0_tmp = p.part(eq0, part, k, w)
    pi_pnn_corr_tmp = p.part(pi_pnn_corr, part, k, w, pf)
    pi_pnd_tmp = p.part(pi_pnd, part, k, w, pf)
    return eq0_tmp - pi_pnn_corr_tmp - pi_pnd_tmp

def eq_pnn_corr_pnd_corr(k, w, pf, part=p.P_DFLT):
    eq0_tmp = p.part(eq0, part, k, w)
    pi_pnn_corr_tmp = p.part(pi_pnn_corr, part, k, w, pf)
    pi_pnd_corr_tmp = p.part(pi_pnd_corr, part, k, w, pf)
    return eq0_tmp - pi_pnn_corr_tmp - pi_pnd_corr_tmp

def eq_pnn_corr_ff_pnd_corr_ff(k, w, pf, part=p.P_DFLT):
    eq0_tmp = p.part(eq0, part, k, w)
    pi_pnn_corr_ff_tmp = p.part(pi_pnn_corr_ff, part, k, w, pf)
    pi_pnd_corr_ff_tmp = p.part(pi_pnd_corr_ff, part, k, w, pf)
    return eq0_tmp - pi_pnn_corr_ff_tmp - pi_pnd_corr_ff_tmp

def d0(k, w, width=1e-2):
    '''Propagator for free pion.'''
    return 1 / (eq0(k, w) - 1j * width)

def d_pnn(k, w, pf, width=1e-2, pi_pnn_part=p.P_DFLT):
    '''Propagator for pNN interacting pion.'''
    return 1 / (eq_pnn(k, w, pf, pi_pnn_part=pi_pnn_part) - 1j * width)

def d_pnn_corr(k, w, pf, width=1e-2, part=p.P_DFLT):
    '''Propagator for pNN interaction with correlations.'''
    return 1 / (eq_pnn_corr(k, w, pf, part=part) - 1j * width)

def d_pnn_corr_pnd(k, w, pf, part=p.P_DFLT, width=1e-2):
    return 1 / (eq_pnn_corr_pnd(k, w, pf, part=part) \
        # + 2j * pi_pnd(k, w, pf).imag \
        - 1j * width)

def d_pnd(k, w, pf, width=1e-2, pi_pnd_part=p.P_DFLT):
    '''Propagator for pND interacting pion.'''
    return 1 / (eq_pnd(k, w, pf, pi_pnd_part=pi_pnd_part) \
        # + 2j * pi_pnd(k, w, pf).imag \
        - 1j * width)

def d(k, w, pf, width=1e-2, part=p.P_DFLT):
    '''Propagator for pion in total.'''
    return 1 / (eq_pnn_pnd(k, w, pf, part=part) - 1j * width)

def d_pnn_corr_pnd_corr(k, w, pf, width=1e-2, part=p.P_DFLT):
    return 1 / (eq_pnn_corr_pnd_corr(k, w, pf, part=part) \
        # + 2j * pi_pnn_corr(k, w, pf).imag \
        + 2j * pi_pnd_corr(k, w, pf).imag \
        - 1j * width)

def d_pnn_corr_ff_pnd_corr_ff(k, w, pf, width=1e-2, part=p.P_DFLT):
    return 1 / (eq_pnn_corr_ff_pnd_corr_ff(k, w, pf, part=part) \
        # + 2j * pi_pnn_corr(k, w, pf).imag \
        + 2j * pi_pnd_corr_ff(k, w, pf).imag \
        - 1j * width)
