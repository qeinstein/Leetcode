class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None

        small_vals = []
        large_vals = []

        current = head
        while current:
            if current.val < x:
                small_vals.append(current.val)
            else:
                large_vals.append(current.val)
            current = current.next

        ll = small_vals + large_vals

        dummy = ListNode(0)
        tail = dummy
        for val in ll:
            tail.next = ListNode(val)  # Attach new node to the list
            tail = tail.next            # Move the tail

        return dummy.next
