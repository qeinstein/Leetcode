# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #this is a stack question, i can use a stack then convert it to the arr then check if its the same back and front
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        print(stack)
        a = ""
        for num in stack:
            a += str(num)
        
        return a == a[::-1]

        # return "".join(stack) = ("".join(stack))[::-1]
        