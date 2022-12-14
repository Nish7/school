#include <stdio.h>

int nthBit(int num, int n)
{
    return (num >> 1) & 1;
}

int setnthBit(int num, int n)
{
    return num | (1 << n);
}

int toggleBit(int num, int i)
{
    return num ^ (num << n)
}

int clearBit(int num, int i)
{
    return num & (~(1 << n));
}

int main(void)
{
    // ^ -> xor
    // ~ -> complement
    // >> -> shift right
    // << -> '' left

    // Just as left shifts are equivalent to multiplying a number by 2,
    // right shifts are equivalent to dividing a number by 2.

    // int has 32 bits while char is 8 bits
    //  a int can be represented as char as well, saving 24 bits

    int num = 27; // 00011011
    printf("Bit 0: %d", nthBit(27, 0));
    printf("Bit 0: %d", nthBit(27, 1));

    return 0;
}