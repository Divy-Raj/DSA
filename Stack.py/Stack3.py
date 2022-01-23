t = int(input())
while(t>0):
    n = int(input())
    count = 0
    for i in range(n):
        n = n//10
        count +=1
    print(count)
    t = t-1