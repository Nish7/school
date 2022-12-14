// Printf Testing
#include <stdio.h>

int main(void) {
    int num1 = 84;
    char ch = 'A';
    double dob = 24.5;

    // Printing as integers:
    printf("num is: %d \n" , num1);
    printf("ch is %c: \n", ch);
    printf("num as ch: %c \n", num1);
    printf("ch as num: %d \n", ch);

    // formating
    printf("It is great outside with: %5d degrees \n ", num1); // %5 means 5 places right justified
    printf("It is great outside with: %-5d degrees \n ", num1); // %5 means 5 places left justified

    //decimal points
    printf("It is great outside with: %-2.3f degrees \n ", dob); // left justifies with 2 places, and 0.3 decimal points of the integer
    
    // mismatched placeholder:
    printf("Printing an integer with float: %f", num1);
    

    return (0);
}