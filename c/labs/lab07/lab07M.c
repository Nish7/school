#include <stdio.h>
#include <math.h>
#include "lab07F.h"
#include <stdlib.h>

int main(void)
{
    int N, max = -999999, min = 9999999, sum;
    scanf("%d", &N);

    if (N == 0)
    {
        return 0;
    }

    int temp;
    while (scanf("%d", &temp) != EOF)
    {
        if (temp > max)
        {
            max = temp;
        }

        if (temp < min)
        {
            min = temp;
        }

        sum += temp;
    }

    double avg = sum / N;

    printTable(N, max, min, avg, sum);

    return 1;
}