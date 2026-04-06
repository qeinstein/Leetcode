# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #this is a stack question, i can use a stack then convert it to the arr then check if its the same back and front
        stack = []
        begin = head
        while begin:
            stack.append(begin.val)
            begin = begin.next

        # print(stack)
        # a = ""
        begin2 = head
        while begin2:
            if begin2.val != stack.pop():
                return False
            begin2 = begin2.next

        return True

        # return "".join(stack) = ("".join(stack))[::-1]
        