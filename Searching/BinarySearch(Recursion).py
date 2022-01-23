def RecBinarySearch(arr,low,high,target):
    if(low>high):
        return
    mid = low+(high-low)//2
    if(arr[mid]==target):
        return mid
    if(arr[mid]<target):
        return RecBinarySearch(arr,mid+1,high,target)
    else:
        return RecBinarySearch(arr,low,mid-1,target)

def main():
    t = int(input())
    while(t>0):
        n = int(input())
        arr = list(map(int,input().split()))
        target = int(input())
        res = RecBinarySearch(arr,0,n-1,target)
        if(res==-1):
            print("Target value is not present")
        else:
            print("Target value is present at index",res)
        t = t-1

if __name__=='__main__':
    main()