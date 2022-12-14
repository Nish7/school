#include <stdio.h>
#include <stdlib.h>

// argc --> number of command lines arguments passed;
// argv --> array of strings; with the arguments itself; first string is the program name
// it ONLY holds strings

int main(int argc, char *argv[])
{

    printf("%s \n", argv[0]);

    // for (int i = 1; i < argc; i++)
    // {
    //     printf("%s \n", argv[i]);
    // }

    int sum = 0;
    for (int i = 1; i < argc; i++)
    {

        // atoi func -> converts string to int
        // atof func -> converts string to double
        sum += atoi(argv[i]);
        printf("%d \n", atoi(argv[i]));
    }

    printf("Sum is %d", sum);

    // return 0;
    exit(0) // sets $? in the shell
}