// list_double.h

#ifndef LIST_DOUBLE_H
#define LIST_DOUBLE_H
#include "list_double.c"

int list_double_push_back(list_double *ld, double el);
list_double *list_double_create(size_t size);
void list_double_delete(list_double **ld);
int list_double_print(list_double *ld);
void list_double_file(FILE *file_output, list_double *ld);
#endif
