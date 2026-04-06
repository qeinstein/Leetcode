# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #brute force approach
        #use an array#
        arr =[]
        while head != None:
            arr.append(head.val)
            head =  head.next

        arr = arr[::-1]
            
        

        dummy = ListNode(0)
        curr = dummy
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy.next