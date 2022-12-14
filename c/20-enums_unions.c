#include <stdio.h>

// ------ ENUMS -----
// the enum values (each day) alias-es their numeric index in the enum;
// sun = 0, mon =1 .... sat = 6

// can specify an index start (sun = 1) and manipulate indexing values;
// can also use char (sun = 'a')

enum day
{
    Sun,
    Mon,
    Tue,
    Wed,
    Thu,
    Fri,
    Sat
};

union point
{
    // stores mulitple variables in same memory location
    // changing one will affect the other
    int x, int y;
};

union overPoint
{

    // can overlop the types, if i store in x , do not read into y, and vice e versa
    int x, float y;
};

int main(void)
{
    // Enums
    for (int i = Sun; i <= sat; i++)
    {
        printf("Day %d \n", i)
    }

    return 0;
}