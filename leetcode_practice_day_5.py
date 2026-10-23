#Write a function second_largest(nums) that returns the second-largest distinct number without using sort() or max().

def second_largest(nums):
   # nums=[1,2,3,4,5,6,7,8,9]
    largest_num =nums[0]
    for i in nums:
        if largest_num < i:
            largest_num = i
            
    return largest_num
  
print(second_largest([1,2,3,4,5,6,7,8,9]))
#print(largest_num)