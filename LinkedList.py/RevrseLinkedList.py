#This is done by iteratively
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail = None

    def insertAtEnd(self,data):
        newNode = Node(data)
        if(self.head is None):
            self.head=newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            self.tail = newNode

    def reverse(self):
        prev = None
        next = None
        curr = self.head
        while(curr is not None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def printSinglyLinkedList(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,end=" ")
           # print(temp,end=" ")
           # print(temp.next)
            temp=temp.next
        print()

    def lengthofLinkedList(self):
        temp = self.head
        count=0
        while(temp is not None):
            count+=1
            temp=temp.next
        return count

def main():
    singlyLinkedList  = LinkedList()
    arr = list(map(int,input().split()))
    for i in range(len(arr)):
        singlyLinkedList.insertAtEnd(arr[i])

    singlyLinkedList.reverse()
    singlyLinkedList.printSinglyLinkedList()

if __name__=='__main__':
    main()