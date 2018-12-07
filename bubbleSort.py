## Bubble sort algorithm in Python

## Function to implement bubble sort
import numpy as np

def bubbleSort(arr):
    def swap(a, b):
        arr[a], arr[b] = arr[b], arr[a]

    length = len(arr)
    isSwapped = True

    x = -1
    while isSwapped:
        isSwapped = False
        x = x + 1
        for i in range(1, length - x):
            if arr[i-1] > arr[i]:
                swap(i-1, i)
                isSwapped = True

    for i in range(0, length):
        print(arr[i])


if __name__ == "__main__":
    arr = np.array([5, 6 , 1, 23, 87, 78, 98, 76])
    bubbleSort(arr)
