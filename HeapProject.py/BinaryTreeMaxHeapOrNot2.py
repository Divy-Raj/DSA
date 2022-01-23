#Here we are checking for Heap not for complete Binary tree
class QueueUsingList:
    def __init__(self):
        self.que = []
        self.size = 0
        self.front = 0

    def enqueue(self,data):
        self.que.append(data)
        self.size+=1
    def isEmpty(self):
        return self.size == 0

    def dequeue(self):
         if(self.isEmpty()):
             print("Queue is Empty")
             return
         temp = self.que[self.front]
         self.front += 1
         self.size -=1
         return temp


    def frontele(self):
        if(self.isEmpty()):
            print("Queue is Empty")
            return
        return self.que[self.front]

    def printQueue(self):
        if(self.isEmpty()):
            print("Queue is Empty")
            return
        for i in range(self.size):
            print(self.que[self.front + i],end=" ")
        print()
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def preOrderTraversal(root):
    if(root is None):
        return
    print(root.data,end=" ")
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)

def isHeap(root):
    if(root is None):
        return True
    queue = QueueUsingList()
    queue.enqueue(root)
    flag = False
    while(queue.size>0):
        temp = queue.dequeue()
        if(temp.left is not None):
            if(flag is True or (temp.left.data>=temp.data)):
                return False
            queue.enqueue(temp.left)
        else:
            flag = True

        if(temp.right is not None):
            if(flag is True or (temp.right.data>=temp.data)):
                return False
            queue.enqueue(temp.right)
        else:
            flag = True
    return True

def main():
    root = Node(10)
    root.left = Node(9)
    root.right = Node(8)
    root.left.left = Node(7)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(4)
    root.left.left.left = Node(3)
    #root.left.left.left.right = Node(80)

    if(isHeap(root)):
        print("Binary Tree is Heap")
    else:
        print("Binary Tree is not Heap")

if __name__=='__main__':
    main()