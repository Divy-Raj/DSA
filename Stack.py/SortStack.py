def insertSorted(stack,value):
    if(len(stack)==0 or value>stack[-1]):
        stack.append(value)
        return

    top = stack.pop()
    insertSorted(stack,value)

    stack.append(top)

def stackSorting():
    if(len(stack)==0):
        return
    top = stack.pop()
    stackSorting(stack)
    insertSorted(stack,top)
def main():
      stack = list(map(int,input().split()))
      stackSorting(stack)
      print("stack before sorting=",stack)
      print("stack after sorting=",stack)

if __name__=="__main__":
    main()