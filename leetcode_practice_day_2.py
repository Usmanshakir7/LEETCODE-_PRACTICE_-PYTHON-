nums =[23,34,56,78,34,45,67,89,20,12,11]
def find_largest_num(nums):
     largest_num = nums[0]
     for num in nums:
         if num > largest_num:
             largest_num = num
             print(f"New largest number found: {largest_num}")
     return largest_num



print(find_largest_num(nums))        