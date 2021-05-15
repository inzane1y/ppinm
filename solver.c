// solver.c

#include <stdio.h>

#include "modules_c/functions.h"
#include "modules_c/list_double.h"
#include "modules_c/root_finding.h"

int main(int argc, char **argv)
{
    rf_func = eq_pnd;
    rf_x0 = 2.4;
    rf_z0 = 1.;
    list_double_print(stripe_bisect_y(0, 6));
    printf("eq(...) = %lf\n", eq_pnd(2.4, 2.166525, 1.));
    /* printf("%d\n", rf_n_bisect); */

    return 0;
}
