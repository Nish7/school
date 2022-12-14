#include <stdlib.h>
#include <stdio.h>
// Calloc and Malloc:
// Are used for allocating memory on the heap
// unlike static arr, they do not get destroyed
// they can be returned from a function

int *tripled(int arr[], int size)
{
    int *arr3 = (int *)calloc(size, sizeof(int));
    // int *arr3 = (int *)malloc(size * sizeof(int)); //calloc are much faster than malloc

    for (int i = 0; i < size; i++)
    {
        arr3[i] = arr[i] * 3;
    }

    return (arr3);
}

int main(void)
{
    int arr[5] = {1, 2, 3, 4, 5};
    int *tripledArr = tripled(arr, 5);

    for (int i = 0; i < 5; i++)
    {
        printf("%d \n", tripledArr[i]);
    }

    // !Always remember to free the array
    free(tripledArr);

    return 0;
}
