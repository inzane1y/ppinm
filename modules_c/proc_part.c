// proc_part.c

#include <complex.h>

double pp_get_part(double complex (*func)(double, complex double, double),
    char p, double x, double y, double z)
{
    switch (p)
    {
        case 'r':
            return creal(func(x, y, z));
        case 'i':
            return cimag(func(x, y, z));
        default:
            return cabs(func(x, y, z));
    }
}
