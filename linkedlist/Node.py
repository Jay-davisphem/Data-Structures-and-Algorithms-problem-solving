class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"Node({self.val})"


def get_node_value(head, index):
    if head == None:
        return None
    if index == 0:
        return head.val
    return get_node_value(head.next, index - 1)


def get_node_value_iter(head, index):
    curr = head
    count = 0
    while curr:
        if count == index:
            return curr.val
        count += 1
        curr = curr.next
    return None


lis = [1, 2, 3, 4, 5, 6, 7, 5, 32, 6, 3, 83, 5, 5, 73, 4, 735, 3, 74, 45, 736, 7]


def list_to_link(lst):
    if len(lst) == 1:
        return Node(lst[0])
    return Node(lst[0], list_to_link(lst[1:]))


def list_to_link_iter(lst):
    cur = dummy = Node(lst[0])
    for i in lst[1:]:
        cur.next = Node(i)
        cur = cur.next
    return dummy


head = list_to_link(lis)

val = get_node_value(head, len(lis) - 1)
print(val)
