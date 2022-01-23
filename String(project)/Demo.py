#Program to print reverse
#n=int(input())
#reverse=0
#while(n>0):
#    remainder=n%10
#    reverse=(reverse*10)+remainder
#    n=n//10
#print(reverse)
#Program to print greater,smaller or equal
#x,y=map(int,input().split())
#if(x>y):
#  print("%d is greater than %d"%(x,y))
#elif(x<y):
#  print("%d is smaller than %d"%(x,y))
#else:
#  print("%d is equal to %d"%(x,y))#
#x,y,z=map(int,input().split())
#if(x>y and x>z):
#  if(y>z):
#    print(y)
#  else:
#    print(z)
#if(y>z and y>x):
#  if(z>x):
#    print(z)
#  else:
#    print(x)
#if(z>x and z>y):
#  if(x>y):
#    print(x)
#  else:
#    print(y)
#ch = input()
#spaces = 8
#for i in range(1,6):
#    for j in range(1,i+1):
#        print(j,end="")
#
#   for k in range(1,spaces+1):
#        print(end=" ")
#    spaces=spaces-2
#
#    for j in range(i,0,-1):
#        print(j,end="")
#    print()
# Birthday gift Problem
#t=int(input())
#while(t>0):
#    a,b,c=map(int,input().split())
#    if(b%c==a):
#        print("Yes")
#    else:
#        print("No")
#    t = t-1
#t=int(input())
#while(t>0):
#    n = int(input())
#    if(n%8==1 or n%8==4):
#        print("LB")
#    elif(n%8==2 or n%8==5):
#        print("MB")
#    elif(n%8==3 or n%8==6):
#        print("UB")
#     elif(n%8==7):
#        print("SL")
#    elif(n%8==0):
#        print("SU")
#    else:
#        print("Wrong Birth")
#    t=t-1

t = int(input())
while(t>0):
    a,b,c = map(int,input().split())
    if(a==b):
        print("Yes")
    elif(a>b and (a-b)%c==0):
        print("Yes")
    elif(a<b and (b-a)%c==0):
        print("Yes")
    elif(a>b and c>0):
        print("No")
    elif(a<b and c<0):
        print("No")
    elif(c==0):
        print("No")
    t=t-1
