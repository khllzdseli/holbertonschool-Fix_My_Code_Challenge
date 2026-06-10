#include "lists.h"
#include <stdlib.h>

int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
    dlistint_t *tmp;
    dlistint_t *current;
    unsigned int i = 0;

    if (head == NULL || *head == NULL)
        return (-1);

    current = *head;

    /* delete head */
    if (index == 0)
    {
        tmp = current;
        *head = current->next;

        if (*head != NULL)
            (*head)->prev = NULL;

        free(tmp);
        return (1);
    }

    while (current && i < index)
    {
        current = current->next;
        i++;
    }

    if (current == NULL)
        return (-1);

    if (current->prev)
        current->prev->next = current->next;

    if (current->next)
        current->next->prev = current->prev;

    free(current);

    return (1);
}
