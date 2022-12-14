#include <stdlib.h>
#include <stdio.h>

int main(void)
{
    // int nums[3][2] = {{1, 2}, {3, 4} ,{5, 6}};
    // m-n matrix

    // in memory it is still in contigous nature
    // memory: 1 2 3 4 5 6 7

    // compsci and eng solution:
    int R = 5, C = 2;
    int *arr = (int *)calloc(R * C, sizeof(int));
    int **mat = (int **)calloc(R, sizeof(int *));

    mat[0] = arr;
    for (int i = 1; i < R; i++)
    {
        mat[i] = mat[i - 1] + C;
    }

    // printing
    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            mat[i][j] = i + j;
            printf("%d \n", mat[i][j]);
        }
    }

    // months[12][10] --> array of strings

    free(arr);
    free(mat);

    return 0;
}
