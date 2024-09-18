import concurrent.futures
import random

def quicksort(arr):
    ##Todo
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [i for i in arr if i < pivot]
    middle = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as e:
        future_left = e.submit(quicksort, left)
        future_right = e.submit(quicksort, right)

    return future_left.result()+middle+future_right.result()
# Example usage:
arr = random.sample(range(1, 100), 20)
print("Original array:", arr)
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)