// find_pfc.c

#include <math.h>
#include <complex.h>
#include <sys/stat.h>
/* #include <unistd.h> */

#include "modules_c/list_double.h"
#include "modules_c/functions.h"

// Flags
int RF_BISECT_NO_ROOTS = 0;

// Function runtime parameters
int rf_axis_imag = 0;
double (*rf_func)(double x, complex double y, double z);
double rf_x0 = 0, rf_y0 = 0, rf_z0 = 0;
double rf_prec_bisect = 1e-4;
double rf_step_strip = 1e-2;
double rf_step_print = 1e-4;
int rf_n_bisect = 1;

double complex make_imag()
{
    return 1 * (1 - rf_axis_imag) + I * rf_axis_imag;
}

// Implemtentation
double rf_double_bisect_y(double y1_arg, double y2_arg)
{
    RF_BISECT_NO_ROOTS = 0;
    double complex y1 = y1_arg * make_imag();
    double complex y2 = y2_arg * make_imag();

    double f_a = rf_func(rf_x0, y1, rf_z0);

    if (f_a * rf_func(rf_x0, y2, rf_z0) >= 0)
    {
        RF_BISECT_NO_ROOTS = 1;
        return 0;
    }

    double complex m = (y2 + y1) / 2.;
    double f_m = rf_func(rf_x0, m, rf_z0);

    for (int i = 0; i < rf_n_bisect; i++)
    {
        if (f_a * f_m < 0)
            y2 = m;
        else
            y1 = m;

        m = (y1 + y2) / 2.;
        f_m = rf_func(rf_x0, m, rf_z0);
    }

    if (fabs(f_m) > 1.)
        RF_BISECT_NO_ROOTS = 1;
    if (rf_axis_imag)
        return cimag(y1 + y2) / 2.;
    return creal(y1 + y2) / 2.;
}

list_double *rf_stripe_bisect_y(double y1, double y2)
{
    double y = y1;
    list_double *roots = list_double_create(3);

    while (y < y2)
    {
        double root = rf_double_bisect_y(y, y + rf_step_strip);
        if (!RF_BISECT_NO_ROOTS)
            if (list_double_push_back(roots, root))
            {
                printf("Error while pushing an element.\n");
                exit(EXIT_FAILURE);
            }

        y += rf_step_strip;
    }

    return roots;
}

int root_found(double x1, double x2, double y1, double y2)
{
    rf_n_bisect = (int)(1. + log(rf_step_strip / rf_prec_bisect) / log(2));
    rf_x0 = x1;

    while (rf_x0 < x2)
    {
        list_double *roots = rf_stripe_bisect_y(y1, y2);

        if (roots->used > 0)
            return 1;

        rf_x0 += rf_step_print;
        list_double_delete(&roots);
    }

    return 0;
}

int main()
{
    rf_axis_imag = 1;
    rf_step_print = 1e-3;
    rf_step_strip = 1e-1;
    rf_prec_bisect = 1e-2;
    rf_z0 = 2.4;
    rf_func = eq_pnd_as;
    while (!root_found(1e-9, 2., 0., 4.) && rf_z0 < 2.7)
        rf_z0 += 1e-4;

    printf("%lf\n", rf_z0);

    return 0;
}
