#include <stdio.h>

void printTable(int N, int max, int min, double avg, int sum)
{
    printf("-----------------------------------");
    printf("\n Number Processed: \t %d \n Maximum: \t\t %d \n Minimum: \t\t %d \n Total: \t\t %d \n Average: \t\t %.2f", N, max, min, sum, avg);
    printf("\n-----------------------------------");
}
