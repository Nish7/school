#include <stdio.h>
#include <string.h>

char *split(char *S, char x)
{
    if (!strchr(S, x))
        return S + strlen(S);

    char *rem = strchr(S, x);
    *rem = '\0';
    rem = rem + 1;

    return rem;
}

int main(void)
{
    char s[] = "abc def ghi jkl";
    char x = 'h';

    char *p = split(s, x);

    printf("S: %s\n", s);
    printf("P: %s", p);

    return 0;
}