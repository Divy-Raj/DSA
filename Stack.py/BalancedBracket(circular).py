class Stack:
    def __init__(self):
        self.arr = []
        self.tos = -1

    def push(self,data):
        self.tos += 1
        self.arr.append(data)

    def pop(self):
        if(self.isEmpty()):
            #print("Stack is empty")
            return
        self.tos = self.tos-1
        self.arr.pop()

    def size(self):
        return self.tos+1

    def isEmpty(self):
        return self.tos==-1

    def top(self):
        if(self.isEmpty()):
            #print("Stack is empty")
            return
        return self.arr[self.tos]

def main():
    st = Stack()
    t = int(input())
    while(t>0):
        str = input()
        flag = 1
        for ele in str:
            if(ele =='('):
                st.push(ele)
            else:
                if(st.isEmpty()):
                    flag = 0
                    break
                st.pop()
        if(st.isEmpty() is False or flag==0):
            print("Bracket is unbalanced")
        else:
            print("Bracket is balanced")

        t=t-1

if __name__=='__main__':
    main()