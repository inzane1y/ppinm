// functions.h

#ifndef FUNCTIONS_H
#define FUNCTIONS_H
#include <complex.h>

#include "functions.c"

double a(double k, double w);
double b(double k, double pf);
double w0(double k);
double complex phi0(double k, double w, double pf);
double complex pi(double k, double w, double pf);
double complex pi_delta(double k, double w, double pf);
double eq0(double k, double w);
double eq_pnn(double k, double w, double pf);
double eq_pnd(double k, double w, double pf);
#endif
