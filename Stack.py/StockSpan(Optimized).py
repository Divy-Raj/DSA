def main():
    t = int(input())
    while(t>0):
        n = int(input())
        arr = list(map(int,input().split()))
        st = []
        st.append(0)
        span = [1]*n
        for i in range(1,n):
            while(len(st)>0 and arr[st[-1]]<=arr[i]):
                st.pop()

            if(len(st)<=0):
                span[i]=i+1
            else:
                span[i]=i-st[-1]
            st.append(i)

        for ele in span:
            print(ele,end=" ")
        print()
        t=t-1
if __name__=="__main__":
    main()