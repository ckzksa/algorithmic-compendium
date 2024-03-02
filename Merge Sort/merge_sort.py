# top-down implementation
import random

def merge_sort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1

    if start >= end:
        return [array[start]]

    middle = (start + end) // 2
    left = merge_sort(array, start, middle)
    right = merge_sort(array, middle+1, end)

    return merge(left, right)


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:] + right[right_index:])
    return result

if __name__ == "__main__":
    array = [random.randint(1, 1000) for _ in range(20)]
    print(f"Shuffled {array}")
    print(f"Sorted   {merge_sort(array)}")