#include "main.h"

/*
struct fileData_s
{
	FILE *file;
	char **file_name;
	char *content;
	int n;
};
typedef struct fileData_s fileData_t;
extern fileData_t fileData;
*/

/**
* main - monty code interpreter
* @argc: number of arguments
* @argv: monty file location
* Return: 0 on success
*/
int main(int argc, char **argv)
{
	int index = 0;

	if (argc != 2)
	{
		printf("ERROR\n");
		exit(EXIT_FAILURE);
	}

	fileData_t file;
	file.n = 10;

	printf("file name is: %d\n", file.n);
	
	
	return (0);
}