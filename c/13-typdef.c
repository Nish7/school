#include <stdio.h>

typedef int integer;

typedef struct ball
{
    char style[10];
    double radius;
    double weight;
} ball;

int main(void)
{
    integer x, y, z;
    x = 1;
    y = 2;
    z = x + y;

    ball b1 = {"Wilson", 3.4, 21.3};

    return 0;
}