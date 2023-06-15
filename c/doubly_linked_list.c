#include "lists.h"

/**
 * print_dlistint - function that prints all the ele of a dlist
 * @head: the node at the beginning of the list
 * Return: Nothing
 */
size_t print_dlistint(dlistint_t *head)
{
	int count = 0;

	if (head == NULL)
		return (count);

	while (head->prev != NULL)
		head = head->prev;

	while (head != NULL)
	{
		printf("%d\n", head->n);
		head = head->next;
		count++;
	}

	return (count);
}

/**
 * dlistint_len - returns the number of elements in a linked list
 * @head: the node at the beginning of the list
 * Return: number of elements
 */
size_t dlistint_len(const dlistint_t *head)
{
	int count = 0;

	if (!head)
		return (count);

	while (head)
	{
		count++;
		head = head->next;
	};

	return (count);
}

/**
 * add_dnodeint - adds a new node at the beginning of a dlistint_t list.
 * @head: the node at the beginning of the list
 * @n:  data to be added to the new node
 * Return: new node address or null
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *new_node;

	/* create a new node */
	new_node = malloc(sizeof(dlistint_t));
	if (!new_node)
		return (NULL);

	/* Insertion the new node at the Beginning of the list */
	new_node->prev = NULL;
	new_node->next = *head;
	new_node->n = n;
	if (*head)
		(*head)->prev = new_node;
	*head = new_node;

	/* Return: new node address */
	return (new_node);
}

/**
 * add_dnodeint_end - adds a new node at the End of a dlistint_t list.
 * @head: the node at the beginning of the list
 * @n:  data to be added to the new node
 * Return: new node address or null
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new_node;

	/* create a new node */
	new_node = malloc(sizeof(dlistint_t));

	if (!new_node)
		return (NULL);
	new_node->next = NULL;
	new_node->n = n;

	if (*head == NULL)
	{
		new_node->prev = NULL;
		*head = new_node;
		return (new_node);
	};

	/* find the last node in the list before insertion a new node at the end */
	while ((*head)->next != NULL)
		*head = (*head)->next;

	/* Insertion the new node at the End */
	new_node->prev = *head;
	(*head)->next = new_node;

	return (new_node);
}

/**
 * free_dlistint - function that frees a dlistint_t list.
 * @h: the node at the beginning of the list
 * Return: Nothing
 */
void free_dlistint(dlistint_t *h)
{
	while (h != NULL)
	{
		dlistint_t *next_node = h->next;

		free(h);
		h = next_node;
	}
}

/**
 * get_dnodeint_at_index - returns the nth node of a dlistint_t linked list
 * @h: the node at the beginning of the list
 * Return: current node or null
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *h, unsigned int idx)
{
	unsigned int counter = 0;

	/* find node by index */
	while (h != NULL)
	{
		h = h->next;
		counter++;
		if (counter == idx)
			return (h);
	}

	/* if index out of the range return null */
	return (NULL);
}

/**
 * sum_dlistint -  returns the sum of all the data(n) of the list
 * @head: the node at the beginning of the list
 * Return: sum = output
 */
int sum_dlistint(dlistint_t *head)
{
	int output = 0;

	while (head != NULL)
	{
		output += head->n;
		head = head->next;
	}

	return (output);
}

/**
 * insert_dnodeint_at_index - inserts a new node at a given position.
 * @head: the node at the beginning of the list
 * @index: position
 * @n: node data
 * Return: new node
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **head, unsigned int index, int n)
{
	/* n_node = new node */
	dlistint_t *ptr = *head, *n_node;
	/* create first node in the list*/
	if (index == 0)
		return (add_dnodeint(head, n));
	/* go to the next node */
	while (index != 1)
	{
		ptr = ptr->next;
		if (ptr == NULL)
			return (NULL);
		index--;
	}
	/* create new node at the end */
	if (ptr->next == NULL)
		return (add_dnodeint_end(head, n));
	/* inserts a new node at a given position. */
	n_node = malloc(sizeof(dlistint_t));
	if (n_node == NULL)
		return (NULL);

	n_node->n = n;
	n_node->prev = ptr;
	n_node->next = ptr->next;
	ptr->next->prev = n_node;
	ptr->next = n_node;
	/* return new node */
	return (n_node);
}