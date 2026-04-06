# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         li_vals = []
#         l2_vals = []

#         current1 = l1
#         current2 = l2
#         while current1:
#             l1_vals.append(current1.val)
#             current1 = current1.next
#         while current2:
#             l2_vals.append(current2.val)
#             current2 = current2.next

#         l1_no = ''.join(str, l1_vals)
#         l2_no = ''.join(str, l2_vals)

#         l1_val = int(l1_no[::-1])
#         l2_val = int(l2_no[::-1])

#         new = l1_val + l2_val

#         l3.val = None

#         if new = 0:
#             return 0
#         else:
#             stri = str(new)[::-1]
#             for c in stri:
                
                
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Create a dummy head node to simplify the logic
        dummy_head = ListNode(0)
        current = dummy_head
        
        # Initialize carry to 0
        carry = 0
        
        # Traverse both lists until both are empty and there is no carry
        while l1 or l2 or carry:
            
            # Get the values of the current nodes, or 0 if a list has ended
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and new carry
            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            new_val = total_sum % 10
            
            # Create a new node and link it to the result list
            current.next = ListNode(new_val)
            current = current.next
            
            # Move to the next nodes in the input lists
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy_head.next

