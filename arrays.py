# 1. Given a binary array, find the maximum number of consecutive 1s in this array.
# Input: [1,1,0,1,1,1]
# Output: 3
def get_max_length(nums):
    length_of_arr = len(nums)
    count = 0
    maximum_count = 0
    for i in range(0, n):
        if length_of_arr[i] == 0:
            maximum_count = 0
        else:
            count += 1
            maximum_count = max(maximum_count, count)
    return maximum_count

# Test Case: nums = [1, 0, 1, 1, 0, 1]
# print(get_max_length(nums))
