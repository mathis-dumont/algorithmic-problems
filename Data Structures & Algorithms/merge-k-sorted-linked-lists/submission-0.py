# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        l1 = lists[0]

        i = 1

        while i < len(lists):
            l2 = lists[i]
            dummy = ListNode(0)
            result = dummy
            
            while l1 and l2:
                if l1.val <= l2.val:
                    result.next = l1
                    l1 = l1.next
                else:
                    result.next = l2
                    l2 = l2.next
                result = result.next

            if l1:
                result.next = l1
            if l2:
                result.next = l2
            l1 = dummy.next
            i+=1
        return l1
        