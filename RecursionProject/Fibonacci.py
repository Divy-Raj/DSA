def fibonacci(n):
    if(n<=1):
        return n
    return (fibonacci(n-1)+fibonacci(n-2))


from sys import setrecursionlimit
setrecursionlimit(11000)
def main():
    n = int(input())
    #print(fibonacci(n))
    for i in range(n):
        print(fibonacci(i))


if __name__=='__main__':
    main()
