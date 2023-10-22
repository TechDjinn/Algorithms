#include <stdio.h>

int linear_search(int element_to_find, int array[], int array_length);

const int N = 7;

int main(void){
    int money_unsorted[7] = {5, 20, 10, 500, 1, 50, 100};
    int element = 50;

    if (linear_search(element, money_unsorted, N) == 1){
        printf("Found %i in the array.\n", element);
    }
    else {
        printf("Did NOT found %i in the array.\n", element);
    }
}

int linear_search(int element_to_find, int array[], int array_length){
    // Check each element in the array. If correct; return 1.
    for (int i = 0; i < array_length; i++){
        if (array[i] == element_to_find){
            return 1;   // Element found!
        }
    }
    // Went through the whole array without finding it. Returning 0.
    return 0;
}