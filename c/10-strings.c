#include <stdio.h>

int main(void)
{
    // strings are arrays of char
    char city[] = "Toronto";

    // arrays of string --> remember to add null char \0
    char city2[] = {'n', 'e', 'w', '\0'};

    printf("%s", city);

    // puts(city); -->  prints a new line after input
    // gets(city); --> take input until new line or eof unlike printf

    // strcpy
    // cannot do s1 = s2
    strcpy(city, city2);
    strcpy(city, "Markham");

    return 0;
}