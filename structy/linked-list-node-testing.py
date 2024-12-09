
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
def linked_list_values(head):
  current = head
  result = []
  while current is not None:    
    result.append(current.val)
    current = current.next

  return result

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

print(linked_list_values(a))


# a = Node("A")        
# b = Node("B")
# c = Node("C")
# d = Node("D")


# a.next = b
# b.next = c
# c.next = d

# def print_linked_list(head):
#     current = head
#     while current is not None:
#         print(current.value, end=" -> ")
#         current = current.next
#     print("None")

# print_linked_list(a)
