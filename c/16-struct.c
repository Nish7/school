#include <stdio.h>
#include <math.h>

struct ball
{
    char style[10];
    double radius;
    double weight;
};

int abc(int x);
double xyz();

int main()
{
    struct ball b1, b3, b5;
    b1.radius = 12.3;
    b1.weight = 1.45;
    strcpy(b1.style "Wilson");

    // struct1 == struct2
    // b3 = b5

    return 0;
}
