// solver.c

#include <stdio.h>
#include <complex.h>
#include <math.h>

#include "modules_c/functions.h"
#include "modules_c/list_double.h"
#include "modules_c/root_finding.h"

double pf = 1.91;
char func_name[100];


void go(double step_k, double step_w, double k1, double k2, double w1, double w2)
{
    rf_axis_imag = 0;
    rf_step_print = step_k;
    rf_step_strip = step_w;

    rf_z0 = pf; // pf
    sprintf(rf_dir_name, "graph_data/%s/%4.3lf", func_name, pf);
    rf_roots_to_file_y(k1, k2, w1, w2);
}

void go_i(double step_k, double step_w, double k1, double k2, double w1, double w2)
{
    rf_axis_imag = 1;
    rf_step_print = step_k;
    rf_step_strip = step_w;

    rf_z0 = pf; // pf
    sprintf(rf_dir_name, "graph_data/%s_i/%4.3lf", func_name, pf);
    rf_roots_to_file_y(k1, k2, w1, w2);
}

int main(int argc, char **argv)
{
    M *= .9;

    sprintf(func_name, "eq_pnn_corr_pnd");
    rf_func = eq_pnn_corr_pnd;

    pf = 1.91; // 1.52, 1.91, 2.19

    double k1 = 1e-7, k_prec = .7, k2 = 3.777;
    double w1 = .98, w_prec = sqrt(1.1), w2 = sqrt(1.1);

    double k1_i = 1.56, k_prec_i = .177, k2_i = 3.725;
    double w1_i = 1e-7, w_prec_i = sqrt(.027), w2_i = sqrt(.031);

    /* go(1e-3, 5e-4, k1, k2, w1, w2); // Low precision everywhere */
    go(5e-4, 5e-8, k1, k_prec, w1, w_prec); // High precision
    /* go(5e-4, 5e-5, k_prec, k2, w1, w2); // Low precision */

    /* go_i(1e-3, 5e-4, k1, k2, w1, w2); // Low precision imaginary axis */
    /* go_i(5e-4, 5e-9, k1_i, k_prec_i, w1_i, w_prec_i); // High precision */
    /* go_i(5e-4, 5e-6, k1_i, k2_i, w1_i, w2_i); // Low precision */

    return 0;
}
