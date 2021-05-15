// solver.c

#include <stdio.h>

#include "modules_c/functions.h"
#include "modules_c/list_double.h"
#include "modules_c/root_finding.h"

int main(int argc, char **argv)
{
    rf_z0 = 1.;
    rf_func = eq_pnd;
    rf_roots_to_file_y(1e-9, 5, 0, 6);

    return 0;
}
