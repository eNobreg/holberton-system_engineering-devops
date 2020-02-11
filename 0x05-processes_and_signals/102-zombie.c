#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
/**
 * infinite_while - Void
 * Return: Int
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Void
 * Return: Int
 */
int main(void)
{
	int i = 0;
	pid_t zombie;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();
		if (zombie > 0)
		{
			printf("Zombie Process %d\n", zombie);
		}
		else
			exit(0);
	}
	infinite_while();
	return (0);
}
