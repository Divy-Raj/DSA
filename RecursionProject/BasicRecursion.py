def printNum(n):
    if(n==0):
        return
    print(n)
    printNum(n-1)


#In python if we want to increase the memory space.Then we have to use import memory according to oue self
from sys import setrecursionlimit
setrecursionlimit(11000)
def main():
    n = int(input())
    printNum(n)

if __name__ =='__main__':
    main()