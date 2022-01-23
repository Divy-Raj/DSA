#t = int(input())
#num = int(input())
#while (t >0):
#    if (num >= 10):
#        num = num // 10
#    else:
#        print(num)
#print(num)
#Box Toy code
n=int(input())
count=0
while(n>0):
    t,c=map(int,input().split())
    if(c-t>=2):
        count+=1
    n=n-1
print(count)