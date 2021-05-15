// root_finding.c

#include <math.h>

#include "list_double.h"

// Flags
int RF_BISECT_NO_ROOTS = 0;

// Function runtime parameters
FILE *rf_file_current_output;
double (*rf_func)(double x, double y, double z);
double rf_x0 = 0, rf_y0 = 0, rf_z0 = 0;
double rf_prec_bisect = 1e-4;
double rf_step_strip = 1e-4;
double rf_step_print = 1e-2;
int rf_n_bisect = 1;

double rf_double_bisect_y(double y1, double y2)
{
    RF_BISECT_NO_ROOTS = 0;

    double f_a = rf_func(rf_x0, y1, rf_z0);

    if (f_a * rf_func(rf_x0, y2, rf_z0) >= 0)
    {
        RF_BISECT_NO_ROOTS = 1;
        return 0;
    }

    double m = (y2 + y1) / 2;
    double f_m = rf_func(rf_x0, m, rf_z0);

    for (int i = 0; i < rf_n_bisect; i++)
    {
        if (f_a * f_m < 0)
            y2 = m;
        else
            y1 = m;

        m = (y1 + y2) / 2;
        f_m = rf_func(rf_x0, m, rf_z0);
    }

    return (y1 + y2) / 2;
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

void rf_roots_to_file_y(double x1, double x2, double y1, double y2)
{
    rf_n_bisect = (int)(1. + log(rf_step_strip / rf_prec_bisect) / log(2));
    double x = x1;
    int flag_after_encounter = 0;
    int branch_counter = 0;
    char file_name[100];

    sprintf(file_name, "graph_data_%d_%4.2lf.txt", branch_counter, rf_z0);
    printf("%s\n", file_name);
    rf_file_current_output = fopen(file_name, "w+");

    while (x < x2)
    {
        rf_x0 = x;
        list_double *roots = rf_stripe_bisect_y(y1, y2);
        fprintf(rf_file_current_output, "%lf", x);
        list_double_file(rf_file_current_output, roots);

        x += rf_step_print;
        list_double_delete(&roots);
    }
}

