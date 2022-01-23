class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class QueueUsingLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size==0

    def enqueue(self,data):
        newNode= Node(data)
        if(self.head is None):
            self.head = self.tail = newNode
            self.size+=1
            return

        self.tail.next = newNode
        self.tail = newNode
        self.size += 1

    def dequeue(self):
        if(self.isEmpty()):
            print("Queue is Empty")
            return
        if(self.size==1):
            temp = self.head.data
            self.head = self.tail = None
            self.size-=1
            return temp

        temp = self.head.data
        self.head = self.head.next
        self.size-=1
        return temp

    def frontele(self):
        if (self.isEmpty()):
            print("Queue is Empty")
            return
        return self.head.data

    def printQueue(self):
        if (self.isEmpty()):
            print("Queue is Empty")
            return

        temp = self.head
        while(temp is not None):
            print(temp.data,end=" ")
            temp = temp.next
        print()

def main():
    que = QueueUsingLinkedList()
    for ele in input().split():
        que.enqueue(int(ele))
    que.printQueue()
    n = 3
    while(n>0):
        print(que.frontele())
        que.dequeue()
        n = n-1
    que.enqueue(100)
    que.printQueue()
    que.enqueue(101)
    que.printQueue()
    que.enqueue(102)
    que.printQueue()
    que.enqueue(103)
    que.printQueue()

if __name__=='__main__':
    main()
