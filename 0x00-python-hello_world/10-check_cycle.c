#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: this is the list to be checked
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *check = list;
	listint_t *checker = list;

	if (!list)
		return (0);
	while (check && checker && checker->next)
	{
		check = check->next;
		checker = checker->next->next;
		if (check == checker)
			return (1);
	}
	return (0);
}
