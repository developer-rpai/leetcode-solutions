class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

 
def reverse_list(head):
  prev = None
  current = head
  print(current.val)

  while current is not None:
    current.next = prev
    current = current.next



a = Node("a")
b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")

a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# a.next = b

print(reverse_list(a))