#include <stdio.h>
#include "lists.h"
size_t print_dlistint(const dlistint_t *h)
{
    size_t c = 0;
    while (h) { printf("%d\n", h->n); h = h->next; c++; }
    return (c);
}
