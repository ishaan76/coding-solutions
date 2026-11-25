
class MyDeque:

    def __init__(self):
        self.dq = []


    def addFront(self, x):
        self.dq.insert(0, x)


    def addBack(self, x):
        self.dq.append(x)


    def removeFront(self):
        if len(self.dq) == 0:
            return -1
        return self.dq.pop(0)


    def removeBack(self):
        if len(self.dq) == 0:
            return -1
        return self.dq.pop()


    def elementAtFront(self):
        if len(self.dq) == 0:
            return -1
        return self.dq[0]


    def elementAtBack(self):
        if len(self.dq) == 0:
            return -1
        return self.dq[-1]


    def isEmpty(self):
        return len(self.dq) == 0


    def size(self):
        return len(self.dq)