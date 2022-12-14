int main(void)
{

    // arrays of 100 of type number;
    int nums[100];
    // empty [] means size will be equal to number of initialized elements
    int num[] = {0, 1, 2, 3};

    // not a compilation error, but a runtime error --> out of bounds
    nums[100] = 12;

    int x = 12;
    // this is ok, in newer version of c
    int numa[x];

    // size cannot be changed!
    nums = nums[200];

    // sizeOf
    // returns the size in bytes of a given data type
    printf("Size of the elements: %f", sizeOf(nums) / sizeOf(int)); // returns number of elements;

    // careful, works in the static arryas declared in the same scope.
    // imagine, passing into the function, an array, rather the whole value, only the pointer to the first element (int*) is passed.

    return 0;
}
