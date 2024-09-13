

def quicksort(arr: list, low: int, high: int)->list:
    def partition(arr, low, high):
        pivot = arr[high] #median_of_three(arr[low],arr[(high+low)//2],arr[high])  # Choose the pivot element (in this implementation, the last element)
        i = low - 1  # Initialize the index of the smaller element
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # Swap arr[i] and arr[j]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap arr[i+1] and arr[high] (pivot)
        return i + 1  # Return the partitioning index
    if low < high:
        # Partition the array and get the partitioning index
        pi = partition(arr, low, high)
        print(arr)
        # Recursively sort elements before partition and after partition
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)
import random

import numpy as np

def quicksort2(arr):
    print(arr)
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = np.array([x for x in arr if x < pivot])
    middle = np.array([x for x in arr if x == pivot])
    right = np.array([x for x in arr if x > pivot])
    return np.concatenate((quicksort2(left), middle, quicksort2(right)))

x=[i for i in range(1,1000+1)]
random.shuffle(x)
quicksort2(x)
print(x)