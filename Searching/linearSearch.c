#include <stdio.h>

int linearSearch(int array[], int size, int target);

int main(void)
{
    // Make an array to search; and a target to find.
    int array[] = {5, 2, 8, 9, 12, 1, 15, 7};
    int size = 8;
    int target = 12;

    // Store index/-1 in variable 'result'; and print message.
    int result = linearSearch(array, size, target);
    if (result != -1)
        printf("Found at index # %i\n", result);
    else
        printf("Did not found!\n");

    return 0;
}

int linearSearch(int array[], int size, int target)
{
    for (int i = 0; i < size; i++)
    {
        // If found: return the index of 'target'
        if (array[i] == target)
            return i;
    }

    // Did not found!
    return -1;
}
