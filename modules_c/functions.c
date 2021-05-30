// functions.c

#include <math.h>
#include <complex.h>
#include "proc_part.h"

// Macros
/* #define M 6.67 */
#define F_DELTA 1.7
#define F 1.
#define W_DELTA 2.1
#define M_STAR .9
#define P0 1.92
#define G_MINUS 1.6

// Runtime variables
char funcs_param_part = 'r';
double M = 6.67;

// Auxiliary functions
double complex a(double k, double complex w)
{
    return w - k * k / (2. * M);
}

double b(double k, double pf)
{
    return k * pf / M;
}

double w0(double k)
{
    return sqrt(1. + k * k);
}

double n0(double pf)
{
    return pf * pf * pf / (6. * M_PI * M_PI);
}

// Main building blocks
double complex phi0(double k, double complex w, double pf)
{
    double complex aa = a(k, w);
    double bb = b(k, pf);

    return M * M * M / (k * k * k * 4. * M_PI * M_PI) * ((aa * aa - 
        bb * bb) / 2. * clog(0. * I + (aa + bb) / (aa - bb)) - aa * bb);
}

double complex phi1_corr(double k, double complex w, double pf)
{
    double complex aa = a(k, w);
    double bb = b(k, pf);

    return M * M / (2 * k * k * k * pf) * ((aa * aa - 
        bb * bb) / 2. * clog(0. * I + (aa + bb) / (aa - bb)) - aa * bb);
}

double complex phi_corr(double k, double complex w, double pf)
{
    return phi1_corr(k, w, pf) + phi1_corr(-k, -w, pf);
}

double complex phi0_as(double k, double complex w, double pf)
{
    return -n0(pf) / a(k, w);
}

// Main functions
double complex pi_pnn(double k, double complex w, double pf)
{
    return -4. * F * F * k * k * 
        (phi0(k, w, pf) + phi0(-k, -w, pf));
}

double complex pi_pnn_as(double k, double complex w, double pf)
{
    return -4. * F * F * k * k * 
        (phi0_as(k, w, pf) + phi0_as(-k, -w, pf));
}

double complex pi_pnd(double k, double complex w, double pf)
{
    return -16. / 9. * F_DELTA * F_DELTA * k * k *
        (phi0(k, w - W_DELTA, pf) + phi0(-k, -w - W_DELTA, pf));
}

double complex pi_pnd_as(double k, double complex w, double pf)
{
    return -16. / 9. * F_DELTA * F_DELTA * k * k *
        (phi0_as(k, w - W_DELTA, pf) + phi0_as(-k, -w - W_DELTA, pf));
}

double complex pi_pnn_corr(double k, double complex w, double pf)
{
    return -2 * M * pf / (M_PI * M_PI) * F * F * k * k * 
        phi_corr(k, w, pf) / (1 + G_MINUS * pf / P0 * phi_corr(k, w, pf));
}

// Convenience functions
double complex eq0(double k, double complex w, double pf)
{
    double w0_tmp = w0(k);
    return w * w - w0_tmp * w0_tmp;
}

double eq_pnd(double k, double complex w, double pf)
{
    double pi_pnd_tmp = pp_get_part(pi_pnd, funcs_param_part, k, w, pf);
    double eq0_tmp = pp_get_part(eq0, funcs_param_part, k, w, pf);
    return eq0_tmp - pi_pnd_tmp;
}

double eq_pnd_as(double k, double complex w, double pf)
{
    double pi_pnd_as_tmp = pp_get_part(pi_pnd_as, funcs_param_part, k, w, pf);
    double eq0_tmp = pp_get_part(eq0, funcs_param_part, k, w, pf);
    return eq0_tmp - pi_pnd_as_tmp;
}

double eq_pnn(double k, double complex w, double pf)
{
    double pi_pnn_tmp = pp_get_part(pi_pnn, funcs_param_part, k, w, pf);
    double eq0_tmp = pp_get_part(eq0, funcs_param_part, k, w, pf);
    return eq0_tmp - pi_pnn_tmp;
}

double eq_pnn_corr(double k, double complex w, double pf)
{
    double pi_pnn_corr_tmp = pp_get_part(pi_pnn_corr, funcs_param_part, k, w, pf);
    double eq0_tmp = pp_get_part(eq0, funcs_param_part, k, w, pf);
    return eq0_tmp - pi_pnn_corr_tmp;
}

double eq_pnn_as(double k, double complex w, double pf)
{
    double pi_pnn_as_tmp = pp_get_part(pi_pnn_as, funcs_param_part, k, w, pf);
    double eq0_tmp = pp_get_part(eq0, funcs_param_part, k, w, pf);
    return eq0_tmp - pi_pnn_as_tmp;
}

double eq_pnn_pnd(double k, double complex w, double pf)
{
    double pi_pnd_tmp = pp_get_part(pi_pnd, funcs_param_part, k, w, pf);
    double pi_pnn_tmp = pp_get_part(pi_pnn, funcs_param_part, k, w, pf);
    double eq0_tmp = pp_get_part(eq0, funcs_param_part, k, w, pf);
    return eq0_tmp - pi_pnn_tmp - pi_pnd_tmp;
}

double eq_pnn_pnd_as_corr(double k, double complex w, double pf)
{
    double eq0_tmp = pp_get_part(eq0, funcs_param_part, k, w, pf);
    double pi_pnn_corr_tmp = pp_get_part(pi_pnn_corr, funcs_param_part, k, w, pf);
    double pi_pnd_as_tmp = pp_get_part(pi_pnd_as, funcs_param_part, k, w, pf);
    return eq0_tmp - pi_pnn_corr_tmp - pi_pnd_as_tmp;
}
