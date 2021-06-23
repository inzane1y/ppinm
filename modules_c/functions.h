// functions.h

#ifndef FUNCTIONS_H
#define FUNCTIONS_H
#include <complex.h>

#include "functions.c"

double n(double pf);
double complex a(double k, double complex w);
double b(double k, double pf);
double w0(double k);
double n0(double pf);
double complex phi0(double k, double complex w, double pf);
double complex phi1_pnn_corr(double k, double complex w, double pf);
double complex phi0_as(double k, double complex w, double pf);
double complex phi_pnn_corr(double k, double complex w, double pf);
double complex pi_pnn(double k, double complex w, double pf);
double complex pi_pnn_as(double k, double complex w, double pf);
double complex pi_pnd(double k, double complex w, double pf);
double complex pi_pnd_as(double k, double complex w, double pf);
double complex pi_pnn_corr(double k, double complex w, double pf);
double complex pi_pnn_corr_ff(double k, double complex w, double pf);
double complex eq0(double k, double complex w, double pf);
double eq_pnd(double k, double complex w, double pf);
double eq_pnd_as(double k, double complex w, double pf);
double eq_pnn(double k, double complex w, double pf);
double eq_pnn_as(double k, double complex w, double pf);
double eq_pnn_corr(double k, double complex w, double pf);
double eq_pnn_pnd(double k, double complex w, double pf);
double eq_pnn_corr_pnd_as(double k, double complex w, double pf);
double eq_pnn_corr_pnd(double k, double complex w, double pf);

double complex a_new(double k, double complex w);
double phi1_pnd_corr(double k, double complex w, double pf);
double complex phi_pnd_corr(double k, double complex w, double pf);
double complex a_delta(double k, double complex w, double pf);
double complex pi_pnd_corr(double k, double complex w, double pf);
double complex pi_pnd_corr_ff(double k, double complex w, double pf);
double eq_pnn_corr_pnd_corr(double k, double complex w, double pf);
double eq_pnn_corr_ff_pnd_corr_ff(double k, double complex w, double pf);
#endif
