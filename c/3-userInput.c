#include <stdio.h>

int main (void) {
    int number;

    scanf("%d", &number); // reads from the input and stores into the number address (&)

    // !BAD:
    // scanf("Here is the number %d:", &number);
    // scanf("%2.3d:", &number);
    // scanf("%d:", number); // !do not forget the address
    // scanf("Here is the number %d:", &number);

    //?Good:
    printf("Enter a number:");
    scanf("%d", &number);
}