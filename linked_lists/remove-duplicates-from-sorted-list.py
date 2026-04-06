class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        seen = {head.val}
        cur = head

        while cur and cur.next:
            if cur.next.val in seen:
                cur.next = cur.next.next
            else:
                seen.add(cur.next.val)
                cur = cur.next

        return head
