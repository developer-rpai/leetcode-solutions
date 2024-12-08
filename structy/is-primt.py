from math import *

def is_prime(n):
    if n <= 1:
        return False
    
    if n == 2 or n == 3:
        return True
    
    for i in range(1, floor(sqrt(n)) + 1):
        if n % i == 0:
            return False


    return True


print(is_prime(8))