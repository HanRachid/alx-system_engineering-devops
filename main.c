#include "shell.h"

int main(void)
{
    char *command = NULL;
    size_t len = 0;
    ssize_t nread;

    while (1)
    {
        printf(":) "); // Prompt
        nread = getline(&command, &len, stdin);
        if (nread == -1)
        {
            free(command);
            exit(EXIT_SUCCESS);
        }

        
        command[nread - 1] = '\0';

        if (strcmp(command, "exit") == 0)
        {
            free(command);
            break;
        }

        execute_command(command);
    }

    return (0);
}
