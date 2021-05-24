// functions.h

#ifndef FUNCTIONS_H
#define FUNCTIONS_H
#include <complex.h>

#include "functions.c"

double complex a(double k, double complex w);
double b(double k, double pf);
double w0(double k);
double n0(double pf);
double complex phi0(double k, double complex w, double pf);
double complex phi0_as(double k, double complex w, double pf);
double complex pi(double k, double complex w, double pf);
double complex pi_as(double k, double complex w, double pf);
double complex pi_delta(double k, double complex w, double pf);
double complex eq0(double k, double complex w, double pf);
double eq_pnd(double k, double complex w, double pf);
double eq_pnn(double k, double complex w, double pf);
double eq_pnn_as(double k, double complex w, double pf);
double eq(double k, double complex w, double pf);
#endif
