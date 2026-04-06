"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # If the head of the linked list does not exist
        # Return None
        if not head:
            return None

        # For the first pass, we interweave the original and copied nodes
        temp = head
        while temp:
            node = Node(temp.val)
            node.next = temp.next
            temp.next = node
            temp = node.next

        """
        1->2->3
        node = a new node with val 1
        node.next = 2(temp.next because temp.next == head)
        temp.next = node    # Now i am confused, why are we saying Node(2).next == 1 which is node?
        temp = node.next (temp is now 2.. understandable)
        """

        # For the second pass: assign random pointers
        temp2 = head
        while temp2:
            node = temp2.next # The copy
            if temp2.random:
                node.random = temp2.random.next
            temp2 = node.next # Move to the next original node

        """
        1->2->3
        node = temp.next (we're saying node.val is 2)
        if temp2.random:    (If it has a random pointer)
            node.random = temp2.random.next # Idk how this works too or the logic behind it
        temp2 = node.next # moving to the next node
        """

        # For the third pass (This is supposed to seperate the two lists)
        newHead = head.next
        temp = head
        while temp:
            node = temp.next
            # Restore original list's next pointer
            temp.next = node.next

            # Set copied list's next pointer
            if node.next:
                node.next = node.next.next

            # Move to the next original node
            temp = temp.next

        """
        I do not understand anything in the third pass at all.
        """

        return newHead


        