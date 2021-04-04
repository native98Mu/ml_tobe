class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None

class SingleCycleLinkList(object):
    def __init__(self):
        self._head = None
    def is_empty(self):
        return self._head is None
    def length(self):

        """链表长度"""
        # 链表为空
        if self.is_empty():
            return 0
        # 链表不为空
        count = 1
        cur = self._head
        while cur.next != self._head:
            count += 1
            # 指针下移
            cur = cur.next
        return count
    def items(self):
        if self.is_empty():
            return
        cur = self._head
        while cur.next != self._head:
            yield cur.item
            cur = cur.next
        yield cur.item
    def add(self,item):
        """头部添加结点"""
        node = Node(item)
        if self.is_empty(): #为空
            self._head = node
            node.next = self._head
        else:
            #添加结点指向head
            node.next = self._head
            cur = self._head
            #移动结点，将末尾结点指向node
            while cur.next != self._head:
                cur = cur.next    
            cur.next = node
    def append(self,item):
        """尾部添加结点"""
        node = Node(item)
        if self.is_empty():#为空
            self._head = node
            node.next = self._head
        else:
            #寻找尾部
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            #尾部指针指向新节点
            cur.next = node
            #新结点指针指向head
            node.next = self._head
    def insert(self,index,item):
        """在指定位置插入一个结点"""
        if index <= 0:
            self.add(item)
        elif index >= self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            #找到所在位置
            for i in range(index - 1):
                cur = cur.next
            #新结点指针指向旧结点
            node.next = cur.next
            #旧结点指针指向新结点
            cur.next = node

    def remove(self,item):
        """删除一个结点"""
        if self.is_empty():
            return
        cur = self._head
        Pre = None
        #第一个元素就是要删除的元素
        if cur.item == item:
            #链表不止一个元素
            if cur.next != self._head:
                while cur.next != self._head:
                    cur = cur.next
                #尾结点指向头结点的下一个
                cur.next = self._head.next
                self._head = self._head.next
            else:
                #只有一个元素
                self._head = None
        else:
            #不是第一个元素 为之间的
            pre = self._head
            while cur.next != self._head:
                if cur.item == item:
                    #删除操作
                    pre.next = cur.next
                    return True
                else:
                    pre = cur #记录前一个指针
                    cur = cur.next #调正指针位置
        #删除元素在末尾
        if cur.item == item:
            pre.next = self._head
            return True

    def find(self,item):
        return item in self.items()

if __name__ == '__main__':
    link_list = SingleCycleLinkList()
    print(link_list.is_empty())
    #头部添加元素
    for i in range(5):
        link_list.add(i)
    print(list(link_list.items()))
    #尾部添加元素
    for i in range(6):
        link_list.append(i)
    print(list(link_list.items()))
    #添加元素
    link_list.insert(3,45)
    print(list(link_list.items()))
    #删除元素
    link_list.remove(5)
    print(list(link_list.items()))
    #元素是否存在
    print(4 in link_list.items())

        
