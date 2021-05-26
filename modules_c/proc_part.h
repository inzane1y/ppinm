// proc_part.h

#ifndef PROC_PART_H
#define PROC_PART_H
#include "proc_part.c"

double pp_get_part(double complex (*func)(double, double complex, double),
    char p, double x, double complex y, double z);
#endif
