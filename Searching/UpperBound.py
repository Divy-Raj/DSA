#If the search element is present it retruns the index of the first element which-
#-is greater then the searched value.(If not present that also same)
#If search element is greater than all elements or its is the last element then it will return index+1
#If search element is less than all the elements it returns the first index.
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

from sys import setrecursionlimit
setrecursionlimit(100000000)
def main():
    t = int(input())
    while(t>0):
        n = int(input())
        arr = list(map(int,input().split()))
        q = int(input())
        while(q>0):
            ele = int(input())
            print(UpperBound(arr,n,ele))
            q =q-1
        t = t-1
if __name__=='__main__':
    main()