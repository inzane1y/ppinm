// solver.c

#include <stdio.h>
#include <complex.h>

#include "modules_c/functions.h"
#include "modules_c/list_double.h"
#include "modules_c/root_finding.h"

int main(int argc, char **argv)
{
    rf_axis_imag = 0;
    rf_step_print = 5e-3;
    rf_step_strip = 1e-2;
    funcs_param_part = 'r';
    rf_func = eq_pnd;

    char func_name[100];
    sprintf(func_name, "eq_pnd_real");

    /* double pf[] = {.89, 1.52, 1.91, 2.19, 2.41}; */
    double pf[] = {2.7};
    int pf_n = 1;
    for (int i = 0; i < pf_n; i++)
    {
        rf_z0 = pf[i]; // pf
        sprintf(rf_dir_name, "graph_data/%s/%5.3lf", func_name, pf[i]);
        rf_roots_to_file_y(1e-9, 5, 0, 8);
    }

    // For imaginary axis
    rf_axis_imag = 1;
    for (int i = 0; i < pf_n; i++)
    {
        rf_z0 = pf[i]; // pf
        sprintf(rf_dir_name, "graph_data/%s_i/%5.3lf", func_name, pf[i]);
        rf_roots_to_file_y(1e-9, 5, 0, 8);
    }

    return 0;
}
