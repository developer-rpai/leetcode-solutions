# def pair_sum(numbers, target_sum):
#     sum = 0 
#     for i in range(len(numbers)):
#         for j in range(i+1,len(numbers)):
#             if numbers[i] + numbers[j] == target_sum:
#                 return (i,j)



# use dictionary to improve O(n)

def pair_sum(numbers, target_sum):
    my_dict = {}
    complement = 0 

    for index, value in enumerate(numbers):
        complement = target_sum - value
        print(complement)

        if complement in my_dict:
            return (my_dict[complement], index)
        
        my_dict[value] = complement



print(pair_sum([6, 4, 2, 8 ], 12) )    