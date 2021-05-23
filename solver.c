// solver.c

#include <stdio.h>
#include <complex.h>

#include "modules_c/functions.h"
#include "modules_c/list_double.h"
#include "modules_c/root_finding.h"

int main(int argc, char **argv)
{
    rf_step_print = 5e-3;
    funcs_param_part_pi = 'r';
    funcs_param_part_pi_delta = 'r';
    rf_func = eq_pnn;

    double pf[] = {.89, 1.52, 1.91, 2.19, 2.41};
    for (int i = 0; i < 5; i++)
    {
        rf_z0 = pf[i]; // pf
        sprintf(rf_dir_name, "graph_data/eq_pnn_real/%4.2lf", pf[i]);
        rf_roots_to_file_y(1e-9, 5, 0, 6);
    }

    return 0;
}
