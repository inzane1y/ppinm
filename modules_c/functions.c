// functions.c

#include <math.h>
#include <complex.h>
#include "proc_part.h"

// Macros
#define M 6.67
#define F_DELTA 1.7
#define F 1.
#define W_DELTA 2.1

// Runtime variables
char funcs_param_part = 'd';

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

double complex phi0_as(double k, double complex w, double pf)
{
    return -n0(pf) / a(k, w);
}

// Main functions
double complex pi(double k, double complex w, double pf)
{
    return -4. * F * F * k * k * 
        (phi0(k, w, pf) + phi0(-k, -w, pf));
}

double complex pi_as(double k, double complex w, double pf)
{
    return -4. * F * F * k * k * 
        (phi0_as(k, w, pf) + phi0_as(-k, -w, pf));
}

double complex pi_delta(double k, double complex w, double pf)
{
    return -16. / 9. * F_DELTA * F_DELTA * k * k *
        (phi0(k, w - W_DELTA, pf) + phi0(-k, -w - W_DELTA, pf));
}

double complex pi_delta_as(double k, double complex w, double pf)
{
    return -16. / 9. * F_DELTA * F_DELTA * k * k *
        (phi0_as(k, w - W_DELTA, pf) + phi0_as(-k, -w - W_DELTA, pf));
}

// Convenience functions
double complex eq0(double k, double complex w, double pf)
{
    double w0_tmp = w0(k);
    return w * w - w0_tmp * w0_tmp;
}

double eq_pnd(double k, double complex w, double pf)
{
    double pi_delta_tmp = pp_get_part(pi_delta, funcs_param_part, k, w, pf);
    double eq0_tmp = pp_get_part(eq0, funcs_param_part, k, w, pf);
    return eq0_tmp - pi_delta_tmp;
}

double eq_pnd_as(double k, double complex w, double pf)
{
    double pi_delta_as_tmp = pp_get_part(pi_delta_as, funcs_param_part, k, w, pf);
    double eq0_tmp = pp_get_part(eq0, funcs_param_part, k, w, pf);
    return eq0_tmp - pi_delta_as_tmp;
}

double eq_pnn(double k, double complex w, double pf)
{
    double pi_tmp = pp_get_part(pi, funcs_param_part, k, w, pf);
    double eq0_tmp = pp_get_part(eq0, funcs_param_part, k, w, pf);
    return eq0_tmp - pi_tmp;
}

double eq_pnn_as(double k, double complex w, double pf)
{
    double pi_as_tmp = pp_get_part(pi_as, funcs_param_part, k, w, pf);
    double eq0_tmp = pp_get_part(eq0, funcs_param_part, k, w, pf);
    return eq0_tmp - pi_as_tmp;
}

double eq(double k, double complex w, double pf)
{
    double pi_delta_tmp = pp_get_part(pi_delta, funcs_param_part, k, w, pf);
    double pi_tmp = pp_get_part(pi, funcs_param_part, k, w, pf);
    double eq0_tmp = pp_get_part(eq0, funcs_param_part, k, w, pf);
    return eq0_tmp - pi_delta_tmp - pi_tmp;
}
