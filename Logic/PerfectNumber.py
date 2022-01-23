t = int(input())
while(t>0):
    sum = 0
    n = int(input())
    for i in range(1,n):
        if(n%i==0):
            sum +=i

    if  (sum == n):
        print("True")
    else:
        print("False")
    t = t-1

