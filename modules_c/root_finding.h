// root_finding.h

#ifndef ROOT_FINDING_H
#define ROOT_FINDING_H
#include "root_finding.c"

double bisect_y(double y1, double y2);
list_double *stripe_bisect_y(double y1, double y2);
void rf_roots_to_file(double x1, double x2, double y1, double y2);
#endif
