
// ! This does not work!
int main(void)
{

    int arr[] = {1, 2, 3, 4, 5, 6};
    int tripledArr[] = returnArr(arr, (sizeOf(arr) / sizeOf(int)));

    for (int i = 0; i < size; i++)
    {
        printf("%d: %d", i, tripledArr[i]);
    }
}

int[] returnArr(int arr[], int size)
{
    int arr2[size];

    for (int i = 0; i < size; i++)
    {
        arr2[i] = arr[i] * 3;
    }

    return arr2;
}