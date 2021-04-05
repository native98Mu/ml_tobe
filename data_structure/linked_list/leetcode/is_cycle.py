# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        cur = head 
        while cur:
            if cur.val == None:
                return True
            else:
                cur.val = None
                cur = cur.next
        return False
        
        