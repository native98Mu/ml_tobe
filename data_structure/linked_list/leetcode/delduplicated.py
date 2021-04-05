# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur = head
        while cur.next != None:
            #前两个元素就重复
            if head.val == head.next.val:
                head = head.next
                cur = head
            #前两个元素不重复
            else:
                if cur.val == cur.next.val:
                    cur.next = cur.next.next
                else:
                    cur = cur.next
            
        return head
            
        