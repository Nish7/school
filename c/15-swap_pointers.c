// without the pointer, the structs get copied in the function hence do not change the given the input.

typedef struct foo
{
    int a, b;
} foo;

void swap(foo *input)
{
    int tmp = foo->a;
    input->a = input->b;
    input->b = tmp;
}

void main()
{
    foo f1 = {1, 2};
    swap(&f1);
}