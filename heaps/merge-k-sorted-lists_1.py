# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        alllinkedlist = []
        for list in lists:
            while list:
                alllinkedlist.append(list.val)
                list = list.next

        alllinkedlist.sort()

        temp = ListNode(0)
        current = temp

        for values in alllinkedlist:
            current.next = ListNode(values)
            current = current.next

        return temp.next