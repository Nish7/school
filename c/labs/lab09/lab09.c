#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>

void incF(int *num, int incval)
{
    *num = *num + incval;
}

int isInt(char *n)
{
    for (int j = 0; j < strlen(n); j++)
    {
        if (n[j] != '-' && !isdigit(n[j]))
            return 0;
    }

    return 1;
}

int main(int argc, char *argv[])
{

    if (!isInt(argv[1]))
        return 1;

    int incN = atoi(argv[1]);

    while (1)
    {
        int temp;
        scanf("%d", &temp);
        incF(&temp, incN);
        printf("%d\n", temp);
    }

    return 0;
}