class Node(object):
    def __init__(self,item):
        self.item = item
        self.prev = None
        self.next = None
    
class BilateralCycleLinkList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None
    def length(self):
        count = 0
        cur = self._head
        if self.is_empty():
            return 
        else:
            while cur.next != self._head:
                cur = cur.next
                count += 1
            return count
    def add(self,item):
        """"""
        