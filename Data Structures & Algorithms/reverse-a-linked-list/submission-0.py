# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # 1 -> 2 -> None
        # head : 1
        # head.next : 2

        # We want : 
        # head : 2
        # head.next : 1
        # head.next.next : None

        cur, prev = head, None

        while cur != None:
            nxt = cur.next
            cur.next = prev
            
            prev = cur
            cur = nxt

        return prev

