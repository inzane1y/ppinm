#include <stdio.h>
#include "modules_c/functions.h"
#include "modules_c/root_finding.h"

int root_found(double x1, double x2, double y1, double y2)
{
    double x = x1;

    while (x < x2)
    {
        rf_x0 = x;
        list_double *roots = rf_stripe_bisect_y(y1, y2);

        /* printf("%lu\n", roots->used); */

        if (roots->used == 0)
        {
            x += rf_step_print;
            list_double_delete(&roots);
            continue;
        }

        list_double_delete(&roots);
        return 1;
    }

    return 0;
}

int main()
{
    rf_axis_imag = 1;
    rf_func = eq_pnn_corr_ff_pnd_corr_ff;
    rf_step_print = 1e-1;
    rf_step_strip = 1e-2;
    rf_n_bisect = (int)(1.0 + log(rf_step_strip / rf_prec_bisect) / log(2.0));

    /* M *= 0.9; */
    /* G_MINUS = 1.6; */
    /* G_DELTA = 0.0; */
    rf_z0 = 0.01;
    while (!root_found(1e-9, 5.0, 0.0, 1.0))
        rf_z0 += 1e-2;

    printf("n(crit) = %.2f n0\npf(crit) = %.2f\n", n(rf_z0), rf_z0);
    return 0;
}
