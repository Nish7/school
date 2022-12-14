#include <stdlib.h>
#include <stdio.h>

typedef struct monkey
{
    char name[10];
    double weight;
    struct monkey *next;
} monkey;

int traverse(monkey *start);

int main(void)
{
    // Linked list initalisation
    int addAnother;
    monkey m1, *curr;
    curr = &m1;

    printf("Name?");
    scanf("%s", curr->name);
    printf("Weight?");
    scanf("%lf", &curr->weight);

    printf("Another? (y=1/n=0)");
    scanf("%d", &addAnother);

    while (addAnother)
    {
        monkey m2;
        curr->next = &m2;
        curr = curr->next;

        printf("Name?");
        scanf("%s", curr->name);
        printf("Weight?");
        scanf("%lf", &curr->weight);
        printf("Another? (y=1/n=0)");
        scanf("%d", &addAnother);
    };

    curr->next = NULL;
    printf("There are %d nodes", traverse(&m1));
    return 0;
}

int traverse(monkey *start)
{
    monkey *p;
    int count = 0;

    for (p = start; p != NULL; p = p->next)
    {
        count = count + 1;
        printf("Monkey %d is %s. \n", count, p->name);
    };

    return count;
}
