from typing import List

# def countdown(n):
#     if n ==0 :
#         return
    
#     print("Before call " + str(n))
#     countdown(n-1)
#     print("After call " + str(n))



# countdown(3)



class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node('A')    
b = Node('B')    
c = Node('C')    
d = Node('D')    

a.next = b
b.next = c
c.next = d


def print_list(head):
    current = head
    while current is not None:
        print(current.val)
        current = current.next


print_list(a)

