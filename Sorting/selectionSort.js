function selectionSort(array) {
	// Using a variable for cleaner code.
	const N = array.length;

	for (let i = 0; i < N; i++) {
		// Find the index of the minimum element in unsorted portion.
		let min_index = i;
		for (let j = i + 1; j < N; j++) {
			if (array[j] < array[min_index]) {
				min_index = j;
			}
		}

		// Swap the minimum element to beginning of unsorted portion.
		let tmp = array[i];
		array[i] = array[min_index];
		array[min_index] = tmp;
	}

	// Return sorted array.
	return array;
}