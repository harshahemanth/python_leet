# 1. Given a binary array, find the maximum number of consecutive 1s in this array.
# Input: [1,1,0,1,1,1]
# Output: 3
def get_max_length(nums):
    length_of_arr = len(nums)
    count = 0
    maximum_count = 0
    for i in range(0, nums):
        if length_of_arr[i] == 0:
            maximum_count = 0
        else:
            count += 1
            maximum_count = max(maximum_count, count)
    return maximum_count


# print(get_max_length(nums))

# -------------------------------------------------------------------------------------------#

# 2. Given an array nums of integers, return how many of them contain an even number of digits.
# Input: nums = [12,345,2,6,7896]
# Output: 2
def find_numbers(nums):
    count_of_even = 0
    for number in nums:
        num_to_string = str(number)
        if len(num_to_string) % 2 == 0:
            count_of_even += 1
    return count_of_even

