def list2link(list_):
    head = Node(list_[0])
    p = head
    for i in range(1,len(list_)):
        p.next = Node(list_[i])
        p = p.next
    return head

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        cur = head
        count = 0
        #将链表元素存放到列表中，记录总共有多少元素
        while cur != None:
            count += 1
            cur = cur.next
        #确定要删除的元素前有多少元素
        num = count - n   
        p = head
        pre = None
        #要删除的是首元素
        if num == 0:
            if count == 1: #如果只有一个元素
                head = None
                return head
            else: #有多个元素
                head = p.next #头指针下移
                return head      
        else:#要删除的不是首元素
            for i in range(num):
                pre = p
                p = p.next  #p->3
            pre.next = p.next
            return head
    

ls = [1,2,3,4,5]
n = 2
s1 = Solution()
print(s1.removeNthFromEnd(list2link(ls),n))