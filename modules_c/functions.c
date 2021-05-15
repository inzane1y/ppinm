// functions.c

#include <math.h>

// Macros
#define M 6.67
#define F_DELTA 1.7
#define F 1
#define W_DELTA 2.1

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

double phi0(double k, double w, double pf)
{
    double aa = a(k, w);
    double bb = b(k, pf);

    return M * M * M / (k * k * k * 4. * M_PI * M_PI) * ((aa * aa - 
        bb * bb) / 2. * log(fabs((aa + bb) / (aa - bb))) - aa * bb);
}

double pi_delta(double k, double w, double pf)
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
    return eq0(k, w) - pi_delta(k, w, pf);
}

