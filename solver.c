// solver.c

#include <stdio.h>
#include <complex.h>
#include <math.h>
#include <sys/stat.h>

#include "modules_c/functions.h"
#include "modules_c/list_double.h"
#include "modules_c/root_finding.h"

double pf = 1.91;
char func_name[100];
char dir_name[200];

void go(double step_k, double step_w, double k1, double k2, double w1, double w2)
{
    sprintf(dir_name, "graph_data/%s", func_name);
    struct stat st = {0};
    if (stat(dir_name, &st) == -1)
        mkdir(dir_name, 0700);

    rf_axis_imag = 0;
    rf_step_print = step_k;
    rf_step_strip = step_w;

    rf_z0 = pf; // pf
    sprintf(rf_dir_name, "graph_data/%s/%4.3lf", func_name, pf);
    rf_roots_to_file_y(k1, k2, w1, w2);
}

void go_i(double step_k, double step_w, double k1, double k2, double w1, double w2)
{
    sprintf(dir_name, "graph_data/%s_i", func_name);
    struct stat st = {0};
    if (stat(dir_name, &st) == -1)
        mkdir(dir_name, 0700);

    rf_axis_imag = 1;
    rf_step_print = step_k;
    rf_step_strip = step_w;

    rf_z0 = pf; // pf
    sprintf(rf_dir_name, "graph_data/%s_i/%4.3lf", func_name, pf);
    rf_roots_to_file_y(k1, k2, w1, w2);
}

int main(int argc, char **argv)
{
    /* M *= 0.9; */

    sprintf(func_name, "eq_pnn");
    rf_func = eq_pnn;

    pf = 2.6; // 1.52, 1.91, 2.19, 2.40

    /* go(1e-1, 1e-5, 1e-9, 5.0, 0.0, 6.0); // unity */
    /* go(1e-2, 1e-4, 1e-9, 0.1, 0.999, 1.5); // alpha */

    go(1e-3, 1e-5, 1e-4, 0.2, 0.0, 0.5); // spin-sound
    go(1e-3, 1e-5, 1e-4, 0.2, 0.8, 1.2); // pi
    /* go(1e-3, 1e-5, 1e-4, 0.2, 2.0, 2.8); // delta */

    go(1e-3, 1e-3, 0.2, 5.0, 0.0, 6.0); // other

    go_i(1e-3, 1e-3, 1e-4, 5.0, 0.0, 2.0);

    return 0;
}
