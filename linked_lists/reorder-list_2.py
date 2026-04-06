# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #ohh, a stack
        #stack.pop after each firse one
        
        stack = []
        ptr = head
        while ptr:
            stack.append(ptr.val)
            ptr = ptr.next

        kk = head

        print(stack)
        n = len(stack)


        ptr = head
        while ptr:
            new_node = ListNode(stack.pop())
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = ptr.next.next

        #now to remove the other half of the ll
        count = 0
        ptr = head
        while count < n - 1:
            ptr = ptr.next
            count += 1
        ptr.next = None

