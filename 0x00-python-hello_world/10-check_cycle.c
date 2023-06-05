#include "lists.h"

/**
 * check_cycle - Check cyclic behavior in a Singly Linked list
 *
 * @list: pointer to head
 *
 * Return: 1 if there is no cycle, 0 if there is cycle
 */	
int check_cycle(listint_t *list)
{
	listint_t *student;
	listint_t *course;

	if (list == NULL)
		return (0);
	student = list;
	course = list;
	while (course->next != NULL && course->next->next != NULL)
	{
		student = student->next;
		course = course->next->next;
		if (student == course)
		{
			student = list;
			while (student != course)
			{
				student = student->next;
				course = course->next;
			}
			return (1);
		}
	}
	return (0);
}
