#This program is to print sum of first n natural numbers
def sumOfN(n):
    if(n==1 or n==0):
        return 1
    return n+sumOfN(n-1)

from sys import setrecursionlimit
setrecursionlimit(11000)
def main():
    n = int(input())
    print(sumOfN(n))


if __name__=='__main__':
    main()
