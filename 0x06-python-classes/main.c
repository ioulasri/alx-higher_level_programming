
void execute_command(char** args, char* cmd, char* buf)
{
    int status;
    pid_t pid = fork();
    if (pid == 0)
    {
        cmd = get_command(args[0]);
        if (cmd)
        {
            execve(cmd, args, NULL);
            free(cmd);
            free_args(args);
            free(buf);
            exit(0);
        }
        else
        {
            write(STDERR_FILENO, "command not found\n", 19);
            free_args(args);
            exit(127);
        }
    }
    else if (pid < 0)
    {
        write(STDERR_FILENO, "Fork failed\n", 12);
    }
    else
    {
        wait(&status);
    }
}

/**
 * main - Entry point of the program
 * Return: Always 0
 */
int main(void)
{
    int status;
    char *buf = NULL;
    size_t buf_size = 0;
    char *cmd, **args;
    pid_t pid;

    signal(SIGINT, handle_interrupt);
    while (1)
    {
        write(STDOUT_FILENO, "$ ", 2);
        args = handle_input(&buf, &buf_size);
        if (args == NULL)
            continue;
        if (strcmp(args[0], "exit") == 0)
        {
            free_args(args);
            free(buf);
            exit(0);
        }
        if (strcmp(args[0], "env") == 0)
            print_env();
        else
            execute_command(args, cmd);
        free_args(args);
    }
    free(buf);
    return 0;
}
