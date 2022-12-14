#include <stdio.h>

// a prototype
int sum_three(int a, int b, int c);

// Funtion must be declared before it is invoked or called.
// Otherwise there might be compile error --> solution, use a prototype
int sum(int n, int n1)
{
    int d = n + n1;
    return d;
}

int main(void)
{
    int n = 2, n1 = 123;
    printf("The Sum of %d and %d is %d", n, n1, sum(n, n1));
    return 0;
}

int sum_three(int a, int b, int c)
{
    int d = a + b + c;
    return d;
}

// void functions --> no return values with no parameters
void stars(void)
{
    printf("*******************\n");
    return; // can still use a return; just for termination
}
