// solver.c

#include <stdio.h>
#include <complex.h>

#include "modules_c/functions.h"
#include "modules_c/list_double.h"
#include "modules_c/root_finding.h"

int main(int argc, char **argv)
{
    rf_z0 = 1.52; // pf
    sprintf(rf_dir_name, "graph_data_eq_pnn_as");
    rf_step_print = 1e-4;
    funcs_param_part_pi = 'r';
    funcs_param_part_pi_delta = 'r';
    rf_func = eq_pnn_as;
    rf_roots_to_file_y(-5 + 1e-9, 5, -6, 6);

    return 0;
}
