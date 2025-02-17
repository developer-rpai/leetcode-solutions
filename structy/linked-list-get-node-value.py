class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def get_node_value(head, index):
  current = head
  counter = 0

  while current is not None:       
    if counter == index:
      return current.val
    counter += 1
    current = current.next

  return None
        
    
    





a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(get_node_value(a, 2)) # 'c'