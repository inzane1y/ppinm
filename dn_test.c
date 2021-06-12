#include <stdio.h>
#include <complex.h>
#include <math.h>

double M = 6.67;

double complex a(double k, double complex w)
{
    return w + k * k / (2.0 * M);
}

double b(double k, double pf)
{
    return k * pf / M;
}

double complex phi1(double k, double complex w, double pf)
{
    double complex aa = a(k, w);
    double bb = b(k, pf);

    return -M * M / (2.0 * k * k * k * pf) * ((aa * aa - bb * bb) / 2.0 * clog((aa + bb) / (aa - bb)) - aa * bb);
}

int main()
{
    M *= 0.9;
    double k = 1e-4, w = 1.0, pf = 1.91;
    printf("phi1 = %.2lf\n", creal(phi1(k, w, pf)));
    return 0;
}
