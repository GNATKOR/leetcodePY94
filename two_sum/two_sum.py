nums = [2, 4, 6, 8, 10, 7]
target = 6


def two_sum(nums_list, target_int):
    for i in nums:
        for j in nums:
            if i+j == target:
                return [nums.index(i), nums.index(j)]


