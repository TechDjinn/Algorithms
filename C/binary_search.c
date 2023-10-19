#include <stdio.h>

int binary_search(int element_to_find, int array_to_search[], int array_length);

const int N = 20;

int main(void)
{
    int number = 50;
    int array[N] = {5, 7, 9, 12, 12, 17, 18, 25, 28, 32,
                    35, 35, 35, 41, 46, 47, 49, 50, 51, 56};

    if (binary_search(number, array, N) == number)
    {
        printf("Found %i in the array.\n", number);
    }
    else
    {
        printf("The number %i was NOT in the array.\n", number);
    }

    return 0;
}

/*
This function implements the Binary Search algorithm to search
a given array for a specified integer ('element_to_find').

Input:
    int element_to_find: the specified integer to find in the sorted array.
    int array_to_search[]: the array that will be search through.
    int array_length: the length of the given array.

Output: The function returns the specified 'element_to_find' if found,
        and -1 if the element is not found in the array.
*/

int binary_search(int element_to_find, int array_to_search[], int array_length)
{
    // Declare the variables for lowest index, middle, and highest index.
    int low = 0;
    int middle;
    int high = array_length - 1;

    while (low <= high)
    {
        middle = (low + high) / 2;

        if (array_to_search[middle] == element_to_find)
        {
            return element_to_find;  // Found it!
        }
        else if (array_to_search[middle] < element_to_find)
        {
            low = middle + 1;  // Search the right half next
        }
        else
        {
            high = middle - 1;  // Search the left half next.
        }
    }
    return -1;  // Element is NOT in the array.
}