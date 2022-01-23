# It is given array is sorted . so i start from 0 and j start from n
def main():
    t = int(input())
    while(t>0):
        n = int(input())
        arr = list(map(int,input().split()))
        k = int(input())
        i = 0
        j = n-1
        while(i<j):
            sum=arr[i]+arr[j]
            if(sum==k):
                flag=1
                print(i,j)
                break
            elif(sum>k):
                j = j-1
            else:
                i=i+1

        if(flag==0):
            print("No answer")
        t=t-1


if __name__ == '__main__':
    main()