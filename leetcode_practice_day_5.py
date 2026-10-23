#Write a function second_largest(nums) that returns the second-largest distinct number without using sort() or max().

def second_largest(nums):
    nums=[1,2,3,4,5,6,7,8,9]
    largest_num =nums[0]
    for i in nums:
        if largest_num > nums:
            largest_num = nums
            print(largest_num)

    return largest_num

second_largest(nums)