#include "shell.h"

void execute_command(char *command)
{
    char *argv[MAX_ARGS];
    char *path, *dir, *cmd_path;
    char *path_env = getenv("PATH");
    int i = 0;
    pid_t pid;

    argv[i] = strtok(command, " ");
    while (argv[i] != NULL && i < MAX_ARGS - 1)
        argv[++i] = strtok(NULL, " ");

    if (argv[0][0] == '/' || argv[0][0] == '.')
    {
        if (access(argv[0], X_OK) == 0)
        {
            pid = fork();
            if (pid == 0)
                execve(argv[0], argv, NULL);
            else
                wait(NULL);
        }
        else
        {
            perror(argv[0]);
        }
        return;
    }

    path = strdup(path_env);
    dir = strtok(path, ":");
    while (dir != NULL)
    {
        cmd_path = malloc(strlen(dir) + strlen(argv[0]) + 2);
        sprintf(cmd_path, "%s/%s", dir, argv[0]);

        if (access(cmd_path, X_OK) == 0)
        {
            pid = fork();
            if (pid == 0)
                execve(cmd_path, argv, NULL);
            else
                wait(NULL);
            
            free(cmd_path);
            free(path);
            return;
        }

        free(cmd_path);
        dir = strtok(NULL, ":");
    }

    fprintf(stderr, "%s: command not found\n", argv[0]);
    free(path);
}
