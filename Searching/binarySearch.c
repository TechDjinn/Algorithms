#include <stdio.h>

int binarySearch(int array[], int size, int target);

int main(void)
{
    // Make an array to search; and a target to find.
    int array_[] = {2, 7, 8, 12, 15, 22, 25, 28};
    int size = 8;
    int target = 12;

    // Store index/-1 in variable 'result'; and print message.
    int result = binarySearch(array_, size, target);
    if (result != -1)
        printf("Found at index # %i\n", result);
    else
        printf("Did not found!\n");

    return 0;
}

int binarySearch(int array[], int size, int target)
{
    // Initialize variables.
    int low = 0;
    int high = size - 1;
    int middle;

    while (low <= high)
    {
        // Calculate next middle.
        middle = (low + high) / 2;

        if (array[middle] < target)
            low = middle + 1;
        else if (array[middle] > target)
            high = middle - 1;
        else
            return middle;
    }

    // Target is NOT in the array.
    return -1;
}
