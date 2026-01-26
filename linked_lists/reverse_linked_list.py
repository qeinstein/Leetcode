"""
reversing a ll is quite an issue but na smalls
It's giving me headache but we shall devour it.

This is the implementation for reversing a linkedlist and a sub linkedlist too
"""

# class Node:
#     def __init__(self, newData):
#         self.data = newData
#         self.next = None

def reversell(head: Optional[ListNode])-> Optional[ListNode]:

    curr = head
    prev = None # initially set to none because we are at the beginning

    # traversing all the nodes of the linkedlist
    while curr is not None:

        # store the next node? Why
        nextNode = curr.next

        # reverse current node's next pointer
        curr.next = prev    # this is set to none initially

        # move pointers one position ahead
        prev = curr
        curr = nextNode

    return prev

    
    # so what we're changing is the pointer dirrection
    # not the relative position of the nodes themselves, Nicee
    


def reverseSUbll(head, right, left):
    