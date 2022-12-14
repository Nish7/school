#include <stdio.h>

int main(void)
{

    //  ?----- if..else statements ----
    bool isTrue = true;
    if (isTrue)
    {
        printf("The condition is true")
    }
    else
    {
        printf("The condition is false buddy!")
    }

    // Everything else in control strucutures in c is basically same as java/js.

    // ?------ switch statements -----
    char cntr = 'd';

    switch (num)
    {
    case 'A':
        printf("Dandelions");
        break; //? Do not forget the break
    case 'B':
        printf("Smile");
        break;
    case 'C':
    case 'd': // Can have multiple cases
        printf("Smile");
        break;
    default: //? remember the default
        printf("Fine!");
    }

    // ?----- loop strucutures -------

    // for loop
    int len = 25;
    for (int i = 0; i < len; i++)
    {
        printf(i);
    }

    // while loop:
    int n = 1;
    while (n < 3)
    {
        printf("%d", n);
        n++;
    }

    // Do while loop
    do
    {
        printf("Hello") // do body will be executed at least once
    } while (n < 3)
}