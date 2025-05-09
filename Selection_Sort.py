def selectionSort(array, size):
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        array[ind], array[min_index] = array[min_index], array[ind]

# Example array
arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
size = len(arr)

# Run selection sort
selectionSort(arr, size)

# Output the sorted array
print('The array after sorting in Ascending Order by Selection Sort is:')
print(arr)
