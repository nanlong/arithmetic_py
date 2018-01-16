from arithmetic_py.linked_list import LinkedList, reverse, reverse2


def test_linked_list():
  linked_list = LinkedList(1, LinkedList(2, LinkedList(3)))
  assert reverse(linked_list).elem == 3

  linked_list = LinkedList(1, LinkedList(2, LinkedList(3)))
  assert reverse2(linked_list).elem == 3