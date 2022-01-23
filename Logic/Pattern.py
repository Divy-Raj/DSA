# printing Pattern
# 1st Question
for i in range(1,6):
    for j in range(1,i+1):
        print(1,end=" ")
    print()
# 2nd Question
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
# 3rd Question
ch = input()
spaces = 8
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")

    for k in range(1,spaces+1):
        print(end=" ")
    spaces = spaces-2

    for j in range(i,0,-1):
        print(j,end=" ")
    print()
