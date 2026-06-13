#include <stdlib.h>
#include "lists.h"
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
    dlistint_t *saved_head = *head;
    unsigned int i = 0;
    if (*head == NULL) return (-1);
    while (saved_head != NULL && i < index) { saved_head = saved_head->next; i++; }
    if (saved_head == NULL) return (-1);
    if (saved_head == *head)
    {
        *head = saved_head->next;
        if (*head != NULL) (*head)->prev = NULL;
    }
    else
    {
        saved_head->prev->next = saved_head->next;
        if (saved_head->next != NULL) saved_head->next->prev = saved_head->prev;
    }
    free(saved_head);
    return (1);
}
