#include <stdio.h>

void fizzbuzz(void);

int main(void)
{
    fizzbuzz();
}

void fizzbuzz(void)
{
    /*
    Description:
        Loop through all numbers 1 <=> 100. 
        If multiple of 3: Print "Fizz"
        If multiple of 5: Print "Buzz"
        If multiple of 15: Print "FizzBuzz"
        Else: Prints the number.
        Function takes no argument and has no return value.
    */
    for (int i = 1; i <= 100; i++)
    {
        if (i % 15 == 0)
        {
            printf("FizzBuzz!\n");
        }
        else if (i % 3 == 0)
        {
            printf("Fizz\n");
        }
        else if (i % 5 == 0)
        {
            printf("Buzz\n");
        }
        else
        {
            printf("%i\n", i);
        }
    }
}