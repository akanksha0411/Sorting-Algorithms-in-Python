import numpy as np

n = int(input('enter the size of the array '))
arr_str = input("Enter the elements of array ").split(" ")
arr = [int(num) for num in arr_str]

print("Original unsorted array ")
print(arr)
print("\n")


def selection_sort(x):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print("Final sorted array using selection sort ")
    print(arr)

if __name__ == "__main__":
    selection_sort(arr)
