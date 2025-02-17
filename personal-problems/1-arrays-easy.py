
from typing import *
# #1
# def max_num(nums:List):
#     max = 0 
#     for num in nums:
#         if num > max:
#             max = num
#     return max
# nums = [1,2,3,4,5,1,3,4,99,1]
# print(max_num(nums))
############################################
#2
# def min_num(nums:List):
#     min = nums[0] 
#     for num in nums:
#         if num < min:
#             min = num
#     return min
# nums = [2,3,4,5,3,4,99]
# print(min_num(nums))
############################################
#3
# def total_sum( nums:List):
#     sum = 0 

#     for num in nums:
#         sum += num
#     return sum
# nums = [1, 3, 12, 0, 0]
# print(total_sum(nums))
############################################
#4
# def avg_sum( nums:List):
#     sum = 0 
#     count = len(nums)
#     for num in nums:
#         sum += num
#     return sum/count
# nums = [1, 2, 3, 4]
# print(avg_sum(nums))
############################################
#5
# def dup(nums:List):
#     myset = set()    
#     for num in nums:
#         myset.add(num)

#     if len(myset) != len(nums):
#         return True
#     return False

# nums = [1, 2, 3, 4,1]
# print(dup(nums))
############################################
#6. Move All Zeroes to the End

# def move_zeros(nums:List):
#     count = 0
#     result = []
#     for num in nums:
#         if num == 0 :
#             count += 1
#         else:
#             result.append(num)    
#     for i in range(0,count):
#         result.append(0)

#     print(result)

# nums = [0, 1, 0, 3, 12]
# print(move_zeros(nums))

############################################
#7 Rearrange Negatives and Positives

# def arrange(nums:List):



# nums = [1, -2, 3, -4, 5] 

############################################
#8 Find the Missing Number
def missing_num(nums:List):

    for i in range(len(nums)-1):
        if nums[i] + 1 != nums[i+1]:
            return nums[i] + 1


nums =  [1, 2, 4, 5] 
print(missing_num(nums))