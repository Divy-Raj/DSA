def UpperBound(arr,n,ele):
    low = 0
    high = n
    while(low<high):
        mid = (low+high)//2
        if(ele>=arr[mid]):
            low = mid+1
        else:
            high = mid
    return low

def main():
    n = int(input())
    arr = list(map(int,input().split()))
    q = int(input())
    while(q>0):
        x = int(input())
        res = UpperBound(arr,n,x)
        print(res)
        q = q-1
if __name__=='__main__':
    main()