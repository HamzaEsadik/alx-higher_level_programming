#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check if there is a cycle
 * @list: linked list to check
 * Return: 0 if there is no list and 1 else
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp;

	tmp = list;
	while (tmp->next != NULL)
	{
		if (tmp->next == list)
		{
			return (1);
		}
		else
		{
			tmp = tmp->next;
		}
	}
	return (0);
}
