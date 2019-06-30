# Sorting-Algorithms-in-Python
I have implemented a few common sorting algorithms in Python. Hope it helps to someone who wants to learn about sorting techniques using Python. Happy coding!

# Bubble Sort Algorithm
I suppose bubble sort is one of the easiest sorting algorithms available at present. Easy to understand and easy to implement. It is an in-place and stable sorting algorithm.
  Bubble sort traverses through the array to be sorted and compares adjacent pairs of elements. If the elements are in wrong order i.e. inverted, they are swapped. This procedure is repeated over through the unsorted portion of the array until the complete array is sorted.
  As bubble sort passes through the unsorted part of the list for every unsorted element, it has a worst case complexity of O(n^2).
  
# Selection Sort Algorithm
The selection sort algorithm sorts an array by repeatedly finding the minimum element from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

1) The sorted sibarray
2) Remaining unsorted subarray.

In every iteration of selection sort, the minimum element from the unsorted subarray is picked and moved to the sorted subarray.

# Insertion sort Algorithm

Insertion sort is both faster and well-arguably more simplistic than both bubble sort and selection sort. On each loop iteration, insertion sort removes one element from the array. It then finds the location where that element belongs within another sorted array and inserts it there. It repeats this process until no input elements remain.

* used when the number of items in the array is less.
* used when the array is nearly sorted

