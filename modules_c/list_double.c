// list_double.c

#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    size_t size;
    size_t used;
    double *array;
} list_double;

int list_double_push_back(list_double *ld, double el)
{
    size_t size = ld->size;
    size_t used = ld->used;

    if (used == size)
    {
        if (size == 0) 
            size++;
        else
            size = size << 1;

        double *tmp = realloc(ld->array, sizeof ld->array * size);
        if (!tmp) return 1;
        ld->size = size;
        ld->array = tmp;
    }

    ld->array[used++] = el;
    ld->used = used;

    return 0;
}

list_double *list_double_create(size_t size)
{
    list_double *tmp;

    tmp = malloc(sizeof *tmp);

    tmp->size = size;
    tmp->used = 0;
    tmp->array = size ? malloc(sizeof tmp->array * size) : NULL;

    return tmp;
}

void list_double_delete(list_double **ld)
{
    free(ld[0]->array);
    free(*ld);
    *ld = NULL;
}

int list_double_print(list_double *ld)
{
    if (!ld)
    {
        printf("list_double_print: NULL value given.\n");
        return 1;
    }

    size_t n = ld->used;
    n == 0 ? printf("[") : printf("[%lf", ld->array[0]);
    for (size_t i = 1; i < n; i++)
        printf(", %lf", ld->array[i]);
    printf("]\n");

    return 0;
}
