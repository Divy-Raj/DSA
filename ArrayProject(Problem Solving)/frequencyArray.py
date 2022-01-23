t = int(input())
while(t>0):
    n = int(input())
    arr = list(map(int,input().split()))
    freq = [0]*40
    for i in range(n):
        freq[arr[i]]+=1

# It is for printing the frequency number of times occur for given number
    #for i in range(40):
    #    if(freq[i]>0):
    #        print(i,freq[i])

# It is for whether the elements present in array are unique or not
    flag = 0
    for i in range(40):
        if(freq[i]>1):
            flag = 1
            break

    if(flag==1):
        print("Elements are not unique")
    else:
        print("Elements are unique")
