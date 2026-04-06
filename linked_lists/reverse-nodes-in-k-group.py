class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1 or not head:
            return head

        dummy = ListNode(0, head)
        groupPrev = dummy

        def reverseSub(start: ListNode, end: Optional[ListNode]):
            prev = end
            curr = start
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev, start  

        while True:
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            groupNext = kth.next

            newHead, newTail = reverseSub(groupPrev.next, groupNext)

            groupPrev.next = newHead
            groupPrev = newTail
