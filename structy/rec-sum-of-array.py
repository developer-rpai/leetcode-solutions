# def sum_numbers_recursive(numbers):
#   if len(numbers) == 0:
#     return 0
#   return numbers[0] + sum_numbers_recursive(numbers[1:])



 

# def factorial(n):  
#     if n == 0:
#         return  1
#     return n * factorial(n-1)


# print(factorial(3));  




def sum_of_lengths(strings):
    if len(strings) == 0 :
        return 0 
    
    return len(strings[0]) +  sum_of_lengths(strings[1:])
   
print(sum_of_lengths(['goat', 'cat', 'purple'])    )