class Node(object):
    """单链表的结点"""
    def __init__(self,item):
        #item存放数据元素
        self.item = item
        #next是下一个节点的标识
        self.next = None

class SingleLinkList(object):
    """单链表"""
    def __init__(self):
        self._head = None
    def is_empty(self):
        """链表是否为空"""
        return self._head is None
    def length(self):
        """"链表长度"""
        #初始指针指向head
        cur = self._head
        count = 0
        #当指针指向None 到达尾部
        while cur is not None:
            count += 1
            cur = cur.next
        return count
    def items(self):
        """遍历链表"""
        #获取head指针
        cur = self._head
        #循环遍历
        while cur is not None:
            #返回生成器
            yield cur.item
            #指针下移
            cur = cur.next
    def add(self,item):
        """向链表头部添加元素"""
        node = Node(item)
        #新结点指针指向原头部结点
        node.next = self._head
        #头部结点修改为新节点
        self._head = node
    def append(self,item):
        """向链表尾部添加元素"""
        node = Node(item)
        #判断链表是否为空
        if self.is_empty():
            #空链表，则添加新节点
            self._head = node
        else:
            #不是空链表，则找到尾部，将尾部结点指向新结点
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
    def insert(self,index,item):
        """向指定位置插入元素"""
        #指定位置在第一个元素之前，头部插入
        if index <= 0:
            self.add(item)
        #指定位置超过尾部，尾部插入
        elif index > (self.length() -  1):
            self.append(item)
        else:
            #创建元素结点
            node = Node(item)
            cur = self._head
            #循环到需要插入的位置
            for i in range(index - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node
    def remove(self,item):
        cur = self._head
        pre = None
        while cur is not None:
            #找到指定元素
            if cur.item == item:
                #如果第一个就是要删除的结点
                if not pre:
                    #将头指针指向头节点后的下一个结点
                    self._head = cur.next
                else:
                    #将删除位置前一个结点的next指向删除位置的后一个结点
                    pre.next = cur.next
                return True
            else:
                #按链表后移
                pre = cur
                cur = cur.next
    def find(self, item):
        """查找元素是否存在"""
        return item in self.items()

def list2link(list_):
    head = Node(list_[0])
    p = head
    for i in range(1,len(list_)):
        p.next = Node(list_[i])
        p = p.next
    return head

class AddTwoNumebrs(object):
    def addtwonumbers(self,l1,l2):
        ll = []
        carry = False
        while l1 != None and l2 != None:
            if carry:
                temp = l1.item + l2.item + 1
                if temp > 9:
                    ll.append(temp-10)
                    carry = True
                else:
                    ll.append(temp)
                    carry = False
            else:
                temp = l1.item + l2.item 
                if temp > 9:
                    ll.append(temp-10)
                    carry = True
                else:
                    ll.append(temp)
            l1 = l1.next
            l2 = l2.next
                
        print(ll)
        while l1 != None:
            if carry:
                temp = l1.val + 1
                if temp > 9 :
                    ll.append(temp-10)
                    carry = True
                else:
                    carry = False
                    ll.append(temp)
            else:
                ll.append(l1.val)
            l1 = l1.next
        while l2 != None:
            if carry:
                temp = l2.val + 1
                if temp > 9 :
                    ll.append(temp-10)
                    carry = True
                else:
                    carry = False
                    ll.append(temp)
            else:
                ll.append(l2.val)
            l2 = l2.next
        if carry:
            ll.append(1)
        print(ll)
        list2link(ll)
        

ls1 = [2]
ls2 = [8]
atn = AddTwoNumebrs()
atn.addtwonumbers(list2link(ls1),list2link(ls2))