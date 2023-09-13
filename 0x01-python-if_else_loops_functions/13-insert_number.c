#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include "lists.h"
/**
 * insert_nodeint_at_index - inserts a new node at idx position
 * @head: pointer to the list
 * @idx: index
 * @n: data
 * Return: adress of new node
 */
listint_t *insert_nodeint_at_index(listint_t **head, int idx, int n)
{
	listint_t *new;
	listint_t *ptr = *head;
	int i;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	return (NULL);
	new->n = n;
	if (idx == 0)
	{
	new->next = *head;
	*head = new;
	return (new);
	}
	for (i = 0; ptr; ++i)
	{
	if (i == idx - 1)
	{
		new->next = ptr->next;
		ptr->next = new;
		return (new);
	}
	ptr = ptr->next;
	}
	free(new);
	return (NULL);
}

/**
 * insert_node - inster note at the correct idx
 * @head: linked list
 * @number: value at the node
 * Return: pointer to new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp;

	if (head != NULL)
	{
		listint_t *tmp;
		int idx;

		idx = 0;
		tmp = *head;
		while (number > tmp->n)
		{
			if (tmp->next == NULL)
			{
				idx++;
				break;
			}
			else
			{
				tmp = tmp->next;
				idx++;
			}
		}
		new = insert_nodeint_at_index(head, idx, number);
		return (new);
	}
	else
		return (NULL);
}
