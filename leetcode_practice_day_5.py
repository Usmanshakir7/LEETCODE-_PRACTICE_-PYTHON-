#Write a function second_largest(nums) that returns the second-largest distinct number without using sort() or max().

# def second_largest(nums):
#    # nums=[1,2,3,4,5,6,7,8,9]
#     largest_num =nums[0]
#     second_num = 0
#     for i in nums:
#         if i > largest_num:
#             second_num = largest_num    
#             largest_num = i
#     return second_num

# print("second_largest no is : ",second_largest([1,2,3,88,90,6,99,8,9]))


# Write a function char_frequency(text) that counts how often each character appears. Ignore spaces and letter case.


def char_frequency(text):
     letters = text.lower()
     fre ={}
     for i in letters :
          if i == " ":
               continue

          if i in fre:
               fre[i]+=1
                
          else:   
               fre[i]=1
            
     print(fre)    
     return fre
      


char_frequency("hello  moto")
         

