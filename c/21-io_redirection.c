#include <stdio.h>

int main(void)
{
    // scanf is the stdin, hence we can redirect a file in stdin
    // $ ./helloWorld < file.txt

    int x, z1, z2;
    // x = scanf("%d%d", &z1, &z2); // inputs 24, returns the number of values sucesfully readsw
    // printf("%d", x);             // prints 1;

    // Reads the stdin/input until eof / ctl-d
    int st;

    while (st != EOF && st != 0) // can also use keyword "EOF" instead of -1
    {
        st = scanf("%d", &x);
        printf("Entered %d \n", x);
    }
}
