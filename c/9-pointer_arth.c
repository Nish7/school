#include <stdio.h>

int main(void)
{
    // nums == &nums[0]
    // nums + i == &nums[i]
    // *(nums + i) = nums[i]

    int i, nums[5];

    for (int i = 0; i < 5; i++)
    {
        *(nums + i) = i * i;
    }

    for (i = 0; i < 5; i++)
    {
        printf("%2d  %d \n", *(nums + i), nums + i);
    }

    return 0;
}