from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
   def find_kth_from_end(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = head
        fast = head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        
        return slow