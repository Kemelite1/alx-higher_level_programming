#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts number into sorted singly linked list
 * @head: pointer
 * @number: this is the number to insert into the linked list
 * Return: a pointer to new node if successful, NULL if fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *newnode;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	if (node == NULL || node->n >= number)
	{
		newnode->next = node;
		*head = newnode;
		return (newnode);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;
	newnode->next = node->next;
	node->next = newnode;
	return (newnode);
}
