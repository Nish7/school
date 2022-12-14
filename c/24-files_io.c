#include <stdio.h>

int main(void)
{
    int tmp, sum = 0;
    FILE *f = fopen("data.txt", "r");

    // Problem: if the there char or strings between the file, when scanning for ints.
    // fscaf would return 0
    int status;

    while (status != EOF)
    {
        status = fscanf(f, "%d", &tmp);

        if (status == 0)
        {
            // it is a char
            char ch;
            printf("Non integer data:");

            do
            {
                fscanf(f, "%c", &ch);
                printf("%c", ch);
            } while (ch != ' ');

            printf("\n");
        }
        else
        {
            sum += tmp;
            printf("%d \n", tmp);
        }
    }

    printf("Sum is: %d", sum);
    // perror("There is also an error!") // fprintf(stderr, "There is an error!");

    // !remember to close the file
    fclose(f);

    return 0;
}
