"""
two pointers, fast and slow technique
"""

# It is also known as floyd's cycle finding algorithm or Hare-Tortoise algorithm


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# this guy lets us know if there's a cycle at all in the ll
def has_cycle(head: Optional[ListNode])-> bool:
    fast = slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            return True

    return False


# this second guy let's us know where exactly the cycle is in the ll
def get_cycle_entrance(head: Optional[ListNode])-> Optional[ListNode]:
    fast = slow = head

    # Detect if a cycle exists ( same thing as above)
    meeting_point = None
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            meeting_point = slow
            break
    
    # If no cycle, return None
    if not meeting_point:
        return None

    # Find the entrance
    # Reset one pointer to the start
    pointer1 = head
    pointer2 = meeting_point
    
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
        
    # The point where they meet is the start of the cycle
    return pointer1