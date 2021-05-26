// solver.c

#include <stdio.h>
#include <complex.h>

#include "modules_c/functions.h"
#include "modules_c/list_double.h"
#include "modules_c/root_finding.h"

int main(int argc, char **argv)
{
    rf_axis_imag = 1;
    rf_step_print = 1e-4;
    rf_step_strip = 1e-2;
    funcs_param_part = 'r';
    rf_func = eq_pnd_as;

    /* double pf[] = {.89, 1.52, 1.91, 2.19, 2.41}; */
    double pf[] = {2.7};
    for (int i = 0; i < 1; i++)
    {
        rf_z0 = pf[i]; // pf
        sprintf(rf_dir_name, "graph_data/eq_pnd_real_i/%4.2lf", pf[i]);
        rf_roots_to_file_y(1e-9, 5, 0, 8);
    }

    return 0;
}
