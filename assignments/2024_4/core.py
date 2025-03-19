import numpy as np

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    smaller = [x for x in arr[1:] if x < pivot]
    greater = [x for x in arr[1:] if x >= pivot]
    return quicksort(smaller) + [pivot] + quicksort(greater)


def quicksort_with_indices(arr, indices):
    if len(arr) <= 1:
        return arr, indices
    pivot_index = 0
    pivot = arr[pivot_index]
    left = []
    right = []
    left_indices = []
    right_indices = []
    for i in range(len(arr)):
        if i == pivot_index:
            continue
        if arr[i] <= pivot:
            left.append(arr[i])
            left_indices.append(indices[i])
        else:
            right.append(arr[i])
            right_indices.append(indices[i])
    sorted_left, left_indices = quicksort_with_indices(left, left_indices)
    sorted_right, right_indices = quicksort_with_indices(right, right_indices)
    return np.concatenate([sorted_left, [pivot], sorted_right]), np.concatenate(
        [left_indices, [indices[pivot_index]], right_indices]
    )
