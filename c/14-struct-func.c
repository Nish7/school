#include <stdio.h>

// takes two basketball structs as arguments as function and compare the radius and the weight, returns 1 if they are the same and 0 if they different

typedef struct ball
{
    double weight;
    double radius;
} baskeball;

int comp(baskeball b1, baskeball b2)
{
    if ((b1.weight == b2.weight) && (b1.radius == b2.radius))
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int main(void)
{
    baskeball b1 = {434.2, 4.2}, b2 = {432.2, 4.2};

    int isEq = comp(b1, b2);
    printf("%d", isEq);

    // it is possible to return an entire struct. unlike arrays, all values are copied.
    return 0;
}