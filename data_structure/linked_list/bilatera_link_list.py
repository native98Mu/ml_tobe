class Node(object):
    def __init__(self,item):
        #item存放数据元素
        self.item = item
        #next 指向下一个结点的标识
        self.next = None
        #prev 指向前一个结点的标识
        self.prev = None
class BilateralLinkList(object):
    """双向链表"""
    def __init__(self):
        self._head = None
    def is_empty(self):
        return self._head is None
    def length(self):
        count = 0
        cur = self._head
        while cur != None:
            count += 1
            cur = cur.next
        return count
    def items(self):
        cur = self._head
        while cur != None:
            #返回生成器
            yield cur.item
            cur = cur.next
    def add(self,item):
        """向头部插入元素"""
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            #新结点指针指向头部结点
            node.next = self._head
            #原头部prev指向新结点
            self._head.prev = node
            #head指向新结点
            self._head = node
    def append(self,item):
        """尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            #新结点向上指针指向旧的尾部
            node.prev = cur
            #旧的尾部指向新节点
            cur.next = node
    def insert(self,index,item):
        """指定位置插入结点"""
        node = Node(item)
        if index <= 0:
            self.add(item)
        elif index > self.length() -1:
            self.append(item)
        else:
            cur = self._head
            for i in range(index - 1):
                cur = cur.next
            #新结点的向下指针指向当前结点
            node.next =cur
            #新结点的向上指针指向当前结点的上一结点
            node.prev = cur.prev
            #当前上一结点的向下指针指向node
            cur.prev.next = node
            #当前结点的向上指针指向node
            cur.prev = node
    def remove(self,item):
        """删除结点"""
        if self.is_empty():
            return
        cur = self._head
        #删除元素在第一个结点
        if cur.item == item:
            #只有一个元素
            if cur.next == None:
                self._head = None
                return True
            else:
                #head指向下一结点
                self._head = cur.next
                #下一结点的向上指针为None
                cur.next.prev = None
                return True
        #
        while cur.next is not None:
            if cur.item == item:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                return True
            cur = cur.next
        #删除元素在最后一个
        if cur.item == item:
            cur.prev.next = None
            return True

    def find(self,item):
        """寻找元素"""
        return item in self.items()

if __name__ == '__main__':
    link_list = BilateralLinkList()
    for i in range(5):
        #头部添加
        link_list.add(i)
    print(list(link_list.items()))
    for i in range(6):
        #尾部添加
        link_list.append(i)
    print(list(link_list.items()))
    #插入
    link_list.insert(3,33)
    print(list(link_list.items()))
    #删除
    link_list.remove(5)
    print(list(link_list.items()))
    #查看元素是否存在
    print(link_list.find(0))
        