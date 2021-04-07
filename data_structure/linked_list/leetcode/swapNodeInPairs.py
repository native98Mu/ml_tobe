
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def list2link(ls):
    head = ListNode(ls[0])
    cur = head
    for i in range(1,len(ls)):
        cur.next = ListNode(ls[i])
        cur = cur.next
    return head
def printLink(head):
    p = head
    while p != None:
        print(p.val, end = ' ')
        p = p.next
    print('\n')
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        evpre = None        
        temp = None
        tempval = None
        count = 0
        #空链表
        if not head:
            return
        #只有一个元素
        if cur.next == None:
            return head  
        #>=2 elements
        pre = cur
        cur = cur.next
        while cur != None:
            print(pre.val)
            print(cur.val)          
            #有2个元素
            if cur.next == None and count == 0:
                tempval = cur.val
                cur.val = pre.val
                pre.val = tempval
                printLink(head)
                return head
            #多于两个
            count += 1
            if count % 2 != 0:
                tempval = cur.val
                cur.val = pre.val
                pre.val = tempval
                printLink(head)               
                pre = cur
                cur = cur.next
            elif count % 2 == 0 and cur.next == None:
                printLink(head)
                return head
            else:
                pre = cur 
                cur = cur.next
                printLink(head)
                    
        return head

ls = [1,2,3,4]
s = Solution()
s.swapPairs(list2link(ls))