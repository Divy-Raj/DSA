#Insertion at front and deletion at front is o(n)
#Insertion at rear and deletion at rear is o(1)
#Dequeue Using list
class  Deque():
    def __init__(self):
        self._dq=[]

    def isEmpty(self):
        return self._dq==[]

    def insertRear(self,data):
        self._dq.append(data)

    def insertFront(self,data):
        self._dq.insert(0,data)

    def deleteRear(self):
        self._dq.pop()

    def deleteFront(self):
        self._dq.pop(0)

    def size(self):
        return len(self._dq)

    def frontEle(self):
        return self._dq[0]

    def rearRele(self):
        return self._dq[-1]

    def printDeque(self):
        for ele in self._dq:
            print(ele,end=" ")
        print()
def main():
    deque = Deque()
    deque.insertFront(5)
    deque.printDeque()
    deque.insertFront(10)
    deque.printDeque()
    deque.insertRear(1)
    deque.printDeque()
    deque.insertRear(12)
    deque.printDeque()
    deque.deleteRear()
    deque.printDeque()
    deque.deleteFront()

    print(deque.frontEle())
    print(deque.rearRele())
    print(deque.size())
    print(deque.isEmpty())

if __name__=='__main__':
    main()
