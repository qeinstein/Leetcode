# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # print(len(head))
        dummy = ListNode(0, head)

        first = second = dummy
        count = 0

        while count <= n:
            second = second.next 
            count += 1

        while second:
            first = first.next
            second = second.next

        first.next = first.next.next
        

        return dummy.next
        