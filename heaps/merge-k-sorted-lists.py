# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # merge everything into one full array, convert that array into a ll after calling .sort()
        vals = []

        for ll in lists:
            curr = ll
            while curr:
                vals.append(curr.val)
                curr = curr.next

        vals.sort()
        dummy = ListNode(0)
        tail = dummy

        for v in vals:
            tail.next = ListNode(v)
            tail = tail.next

        return dummy.next

        