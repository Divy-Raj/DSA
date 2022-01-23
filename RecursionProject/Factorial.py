#we use induction input method to do this type of recusion.In this method we use three steps
#(1) For smaller input we create output i.e for fact(1) = 1
#(2) Assume fact(n-1)
#(3) fact(n) = n*fact(n-1)
def fact(n):
    if(n==0 or n==1):
        return 1
    return n*fact(n-1)



from sys import setrecursionlimit
setrecursionlimit(11000)
def main():
    n = int(input())
    print(fact(n))


if __name__=='__main__':
    main()