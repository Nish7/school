#include <stdio.h>

int main(void)
{
    int number;
    scanf("%d", &number);

    // ? pointer is a variable that stores the address of another variable:
    int *intrl;

    // ? derefrencing
    char c1 = 'A', c2;
    char *ptr = &c1;
    c2 = *ptr;
    *ptr = 'C';
}

// pointer as paramaeters:
void quadForm(double a, double b, double c, double *x1, double *x2);

int main(void)
{
    double a = 1.1, b = 2.2, c = 2.5;
    double root1, root2;

    quadForm(a, b, c, &root1, &root2);
    printf("Roots: %lf %lf", root1, root2);
    return 0;
}