# Task 1: Implement a binary search algorithm to find the position of a target value within a sorted list
def binary_search(arr,target):
    left,right = 0, len(arr) - 1

    while left <= right:
        mid = left+(right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid +1
        else: 
            right = mid -1
    return -1

sorted_list = [1,2,3,4,5,6,7,8,9,10]
target_value = 7
result = binary_search(sorted_list,target_value)
if result != -1:
    print(f"Element found at the index of : {result}")
else:
    print("Element not found in the given list")