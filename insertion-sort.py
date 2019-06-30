import numpy as np

n = int(input('enter the size of the array '))
arr_str = input("Enter the elements of array ").split(" ")
arr = [int(num) for num in arr_str]

print("Original unsorted array ")
print(arr)
print("\n")


for i in range(len(arr)):
    print(arr[i])

def insertion_sort(x):
    for i in range(len(x)):
        cursor = x[i]
        posi = i

        while(posi>0 and x[posi-1]> cursor):
            arr[posi] = arr[posi-1]
            posi = posi-1
        arr[posi] = cursor
    print(x) 

if __name__ == "__main__":
    insertion_sort(arr)
