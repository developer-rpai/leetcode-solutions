from math import *

def is_prime(n):
    if n == 2 or n == 3 or n ==5 or n == 7:
        return True
    if n < 2:
        return False
    if n % 2 == 0 :
        return False
    if n % 3 == 0 :
        return False
    if n % 5 == 0 :
        return False    
    if n % 7 == 0 :
        return False
    return True

print(is_prime(5))