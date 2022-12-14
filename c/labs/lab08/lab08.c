#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define MAX 100

// 0  1  2  3  4
// {d, r, i,v, e}

void printBackwards(char S[])
{
    int len = strlen(S);
    printf("Backward: ");
    for (int j = len - 1; j != -1; j--)
    {
        printf("%c", S[j]);
    }
}

void squeeze(char c, char S[])
{

    for (int i = 0; S[i] != '\0'; i++)
    {

        if (S[i] == c)
        {
            for (int j = i; S[j]; j++)
            {
                S[j] = S[j + 1];
            }

            i--;
        };
    }

    printf("Forward: %s \n", S);
    printBackwards(S);

    return;
}

int main()
{
    char ch;
    char str[MAX];

    printf("Input a char: ");
    scanf("%c", &ch);
    getc(stdin);

    printf("Input a string (length of max 100): ");
    fgets(str, MAX, stdin);

    str[strlen(str) - 1] = '\0';

    squeeze(ch, str);

    return 0;
}
