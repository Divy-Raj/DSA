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

class Stack:
    def __init__(self):
        self.arr = []
        self.tos = -1

    def push(self,data):
        self.tos +=1
        self.arr.append(data)

    def pop(self):
        if(self.isEmpty()):
            print("Stack is Empty")
            return
        self.tos = self.tos-1
        self.arr.pop()

    def size(self):
        return self.tos+1

    def isEmpty(self):
        return self.tos==-1

    def top(self):
        if(self.isEmpty()):
            print("Stack is Empty")
            return
        return self.arr[self.tos]

def main():
    que = QueueUsingList()
    st = Stack()
    for ele in input().split():
        que.enqueue(int(ele))

    while(que.isEmpty() is False):
        st.push(que.dequeue())

    while(st.isEmpty() is False):
        que.enqueue(st.top())
        st.pop()

    que.printQueue()



if __name__=='__main__':
    main()