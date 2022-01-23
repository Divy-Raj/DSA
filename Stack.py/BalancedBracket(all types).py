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
    t = int(input())
    while(t>0):
        st = Stack()
        str = input()
        flag = 1
        for ele in str:
            if(ele=='('or ele=='{'or ele=='['):
                st.push(ele)
            else:
                if(st.isEmpty()):
                    flag = 0
                    break
                if((st.top()=='(' and ele==')') or (st.top()=='{' and ele=='}') or (st.top()=='[' and ele==']')):
                    st.pop()
                else:
                    flag = 0
                    break
        if(st.isEmpty()==False or flag==0):
            print("Bracket is Unbalanced")
        else:
            print("Bracket is Balanced")
        t=t-1

if __name__=='__main__':
    main()