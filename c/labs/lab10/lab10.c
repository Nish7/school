#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int isInt(char *S)
{
    for (int i = 0; i < strlen(S); i++)
    {
        if (S[i] != '-' && !isdigit(S[i]))
            return 0;
    }

    return 1;
}

int main(int argc, char *argv[])
{
    // <integer> <infile> <outfile>
    FILE *infile = fopen(argv[2], "r");
    FILE *outfile = fopen(argv[3], "w");

    // error checking
    if (argc != 4 || !isInt(argv[1]) || infile == NULL)
        return 1;

    int incN = atoi(argv[1]);

    int n;
    while (fscanf(infile, "%d", &n) != EOF)
    {
        fprintf(outfile, "%d\n", n + incN);
    }

    // closing file
    fclose(infile);
    fclose(outfile);
}