class LinkedList:

  def __init__(self, elem, node=None):
    self.elem = elem
    self.next = node


def reverse(linked_list):
  if not linked_list or not linked_list.next:
    return linked_list

  pre = None
  cur = linked_list

  while cur:
    tmp = cur
    cur = cur.next
    tmp.next = pre
    pre = tmp

  return pre


def reverse2(linked_list):
  if not linked_list or not linked_list.next:
    return linked_list

  new_list = reverse2(linked_list.next)
  linked_list.next.next = linked_list
  linked_list.next = None
  return new_list

if __name__ == '__main__':
    linked_list = LinkedList(1, LinkedList(2, LinkedList(3)))
    print reverse(linked_list).elem

    linked_list = LinkedList(1, LinkedList(2, LinkedList(3)))
    print reverse2(linked_list).elem
    