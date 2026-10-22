student ={
    "name":"usman",
    "age": 20,
    "marks": 90
}

print(student["name"],student["marks"])
student["marks"] = 95
print(student)

# Create the list nums,Convert it into a set,Store the result in a variable named unique_nums.
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = set(nums)
print(unique_nums)

#Write a function called count_frequency(nums) that returns a dictionary counting each number.

def count_frequency(nums):
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num]+=1
        else:
            frequency[num]=1
    return frequency

print(count_frequency(nums))


# Write a function has_duplicates(nums) that returns:
# - True if any number appears more than once.
# - False if every number is unique.
 
def has_duplicates(nums):
    if len(nums)!=len(set(nums)):
        return True
    else:
        return False
   
print(has_duplicates(nums))