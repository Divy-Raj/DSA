class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def InsertAtEnd(self,data):
        newNode = Node(data)
        if(self.head is None):
            self.head=newNode
            self.tail=newNode
            return

        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode

    def InsertAtBeginning(self,data):
        newNode = Node(data)
        if (self.head is None):
            self.head = newNode
            self.tail = newNode
            return

        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode

    def InsertAtGivenPosition(self,i,data):
        newNode = Node(data)
        n = self.lengthofLinkedList()
        if(i==0):
            self.InsertAtBeginning(data)
            return
        if(i==n):
            self.InsertAtEnd(data)
            return
        if(i>n):
            print("Invalid Position")
            return
        count=0
        temp = self.head
        while(temp.next is not None and count is not (i-1)):
            count+=1
            temp = temp.next
        newNode.prev = temp
        newNode.next = temp.next
        temp.next.prev =  newNode
        temp.next = newNode



    def printDoublyLinkedList(self):
        temp=self.head
        while (temp is not None):
            #print(temp.prev, end=" ")
            print(temp.data, end=" ")
            #print(temp, end=" ")
            #print(temp.next)
            temp = temp.next
            print()

    def lengthofLinkedList(self):
        temp=self.head
        count =0
        while(temp is not None):
            print(temp.data,end=" ")
            temp = temp.next

        return count

def main():
    doublyLinkedList = DoublyLinkedList()
    arr = list(map(int,input().split()))
    for i in range(len(arr)):
        doublyLinkedList.InsertAtBeginning(arr[i])
    doublyLinkedList.InsertAtGivenPosition(3,100)
    doublyLinkedList.printDoublyLinkedList()
    doublyLinkedList.InsertAtGivenPosition(0,100)
    doublyLinkedList.printDoublyLinkedList()
    doublyLinkedList.InsertAtGivenPosition(6,100)
    doublyLinkedList.printDoublyLinkedList()



if __name__ =='__main__':
    main()