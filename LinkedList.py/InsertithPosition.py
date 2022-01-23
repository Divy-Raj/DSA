#Insert at ith position of given Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtEnd(self, data):
        newNode = Node(data)
        if (self.head is None):
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            self.tail = newNode

    def insertAtBeginning(self, data):
        newNode = Node(data)
        if (self.head is None):
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertAtithPosition(self,i,data):
        newNode = Node(data)
        if(i==0):
            self.insertAtBeginning(data)
        else:
            count=0
            temp=self.head
            while(temp.next is not None and count is not(i-1)):
                count+=1
                temp=temp.next
            if(temp.next is  None and i>count+1):
                return
            else:
                newNode.next=temp.next
                temp.next=newNode

    def printSinglyLinkedList(self):
        temp = self.head
        while (temp is not None):
            print(temp.data, end=" ")
            # print(temp,end=" ")
            # print(temp.next)
            temp = temp.next
        print()


def main():
    singlyLinkedList = LinkedList()
    singlyLinkedList2 = LinkedList()
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        singlyLinkedList.insertAtBeginning(arr[i])
        singlyLinkedList2.insertAtEnd(arr[i])

#At the Zeroth position we insert 100
    singlyLinkedList2.insertAtithPosition(0,100)
    singlyLinkedList.printSinglyLinkedList()
    singlyLinkedList2.printSinglyLinkedList()


if __name__ == '__main__':
    main()

# This code has time complexity o(1)
