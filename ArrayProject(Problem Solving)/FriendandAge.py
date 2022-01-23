n = int(input())
a = list(map(int,input().split()))
count = 0
for i in range(n):
    for j in range(n):
       if(i!=j):
           if((a[j]<-0.5*a[i]+7) or (a[j]>100 and a[i]<100) or (a[j]>a[i])):
               continue
           else:
                count+=1

print(count)