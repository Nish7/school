#include <stdio.h>

int main(void)
{
    int as = -3;

    // ?----- unary operators: -------
    printf("The number is: %d \n", as);
    printf("The number is: %d \n", -as);

    // ?------ integer expressions: ------
    int x = 22, y = 33;
    double res = x / y; // result of an integer exp, is always int
    // non-integers results are trucated, and happens *before* being stores in result.

    printf("the result: %lf \n", res);

    // result of a mixed expre (floating point and integer) will be floating point
    double d = 24.3, resa;
    int i = 12;

    resa = d * i;

    printf("the result: %lf \n", resa);

    // ?--------  Typecasting: -----
    printf("%lf \n", x / y);
    printf("%lf \n", (double)x / y);
    printf("%lf \n", (double)(x / y));
    printf("%lf \n", x / (double)y);

    // ?------ i++ ------
    int a = 1, c = 2, r, r1;
    r1 = ++a;
    r = b++;

    printf("Pre: %d", r1); // pre-increment: increment, then evaluate and assign
    printf("Post: %d", r); // post-increment: evaluate and then increment

    return (0);
}