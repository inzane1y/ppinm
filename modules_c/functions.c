// functions.c

#include <math.h>
#include <complex.h>
#include "proc_part.h"

// Macros
#define M 6.67
#define F_DELTA 1.7
#define F 1
#define W_DELTA 2.1

// Runtime variables
char funcs_param_part_pi_delta = 'd';
char funcs_param_part_pi = 'd';

// Implementations
double a(double k, double w)
{
    return w - k * k / (2 * M);
}

double b(double k, double pf)
{
    return k * pf / M;
}

double w0(double k)
{
    return sqrt(1 + k * k);
}

double complex phi0(double k, double w, double pf)
{
    double aa = a(k, w);
    double bb = b(k, pf);

    return M * M * M / (k * k * k * 4. * M_PI * M_PI) * ((aa * aa - 
        bb * bb) / 2. * clog(0 * I + (aa + bb) / (aa - bb)) - aa * bb);
}

double complex pi(double k, double w, double pf)
{
    return -4 * F * F * k * k * 
        phi0(k, w, pf) + phi0(-k, -w, pf);
}

double complex pi_delta(double k, double w, double pf)
{
    return -16. / 9. * F_DELTA * F_DELTA * k * k *
        (phi0(k, w - W_DELTA, pf) + phi0(-k, -w - W_DELTA, pf));
}

double eq0(double k, double w)
{
    double w0_tmp = w0(k);
    return w * w - w0_tmp * w0_tmp;
}

double eq_pnd(double k, double w, double pf)
{
    double pi_delta_tmp = pp_get_part(pi_delta, funcs_param_part_pi_delta, k, w, pf);
    return eq0(k, w) - pi_delta(k, w, pf);
}

double eq_pnn(double k, double w, double pf)
{
    double pi_tmp = pp_get_part(pi, funcs_param_part_pi, k, w, pf);
    return eq0(k, w) - pi(k, w, pf);
}

double eq(double k, double w, double pf)
{
    double pi_delta_tmp = pp_get_part(pi_delta, funcs_param_part_pi_delta, k, w, pf);
    double pi_tmp = pp_get_part(pi, funcs_param_part_pi, k, w, pf);
    return eq0(k, w) - pi_delta_tmp - pi_tmp;
}

