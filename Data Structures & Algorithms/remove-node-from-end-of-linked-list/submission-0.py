# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        cur, prev = head, None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        if n == 1:
            dummy = prev.next
        else:
            c=1
            dummy = prev
            while prev:
                if c==n-1:
                    prev.next = prev.next.next
                c+=1
                prev = prev.next
        
        cur2, prev2 = dummy, None
        while cur2:
            nxt2 = cur2.next
            cur2.next = prev2
            prev2 = cur2
            cur2 = nxt2
        
        return prev2




        
        