import concurrent.futures
import random
import time


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    left_ind = 0
    right_ind = 0

    while left_ind < len(left) and right_ind < len(right):
        if left[left_ind] < right[right_ind]:
            result.append(left[left_ind])
            left_ind += 1
        else:
            result.append(right[right_ind])
            right_ind += 1

    result.extend(left[left_ind:])
    result.extend(right[right_ind:])

    return result




def parallel_merge_sort(arr, maxWorkers):
    if len(arr) <= 1:
        return arr

    # mid = len(arr)//2
    # left = arr[:mid]
    # right = arr[mid:]

    with concurrent.futures.ProcessPoolExecutor(max_workers=maxWorkers) as executor:
        left_future = executor.submit(merge_sort, arr)
        # right_future = executor.submit(merge_sort, right)

        left_arr = left_future.result()
        # right_arr = right_future.result()

    return merge(left_arr, left_arr)



if __name__ == '__main__':
    start_time = time.time()

    arr = [random.randint(0,1000) for i in range(1000000)]
    max_worker = 3
    # print(arr)
    sorted_arr = parallel_merge_sort(arr, max_worker)

    end_time = time.time()

    print(start_time, end_time)
    print(f"Execution time {end_time-start_time}")