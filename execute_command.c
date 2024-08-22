#include "shell.h"
/**
 * exeCommandLine - Executes a command using the fork-exec model.
 * @argv: An array of strings (command and its arguments) to be executed.
 *
 * This function creates a child process using fork().
 * The child process then attempts to execute the command specified in argv[0]
 * using execve(). If the execve() call fails, the function returns -1.
 * The parent process waits for the child to complete execution and returns 0
 * if successful. In case of fork() failure, the function returns -1.
 * If everything is successful, it returns 2 (although this is unreachable in
 * the current implementation).
 *
 * Return: -1 on fork() or execve() failure, 0 on successful execution.
 */
int exeCommandLine(char *argv[MAX_ARGS])
{
	int fflag = 0;
	/* ------------------fork to child execve-------------------------*/
	fflag = fork();

	if (fflag == -1)
	{
				/*printf("fealuire");*/
		return (-1);
	}
	else if (fflag == 0)
	{
		/* --------------------------child execve--------------------*/
		if (execve(argv[0], (char **)argv, NULL) == -1)
		{
			/*printf("No such file or directory\n");*/
			return (-1);
		}
	}
	else
	{
		/* --------------------------wait child execve--------------------*/
		wait(NULL);
		return (0);
	}
	return (2);
}
