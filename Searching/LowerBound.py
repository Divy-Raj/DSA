#If there are multiple occurence of searched element it returns the index of first occurence
#If the search element is not present it returns the index if next greater element
#If search element is greater than all elements it returns the last index+1
#If search element is less than all the elemnts it  returns the index of first element
def lowerBound(arr,n,ele):
    low = 0
    high = n
    while(low<high):
        mid = (low+high)//2
        if(ele<=arr[mid]):
            high = mid
        else:
            low = mid+1
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
            print(lowerBound(arr,n,ele))
            q =q-1
        t = t-1
if __name__=='__main__':
    main()