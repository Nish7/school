#include <stdlib.h>
#include <string.h>
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
    monkey *start;
    monkey m1, m2, m3;

    start = &m1;

    strcpy(m1.name, "Monu");
    strcpy(m2.name, "Chomu");
    strcpy(m3.name, "Tomu");

    m1.weight = 20.0;
    m2.weight = 30.0;
    m3.weight = 20.0;

    m1.next = &m2;
    m2.next = &m3;
    // Dont forget last null
    m3.next = NULL;

    // ----- Traversal -----
    int cnt = traverse(start);
    printf("Found %d nodes", cnt);

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
