#Function is block of code which used in reuseability of code
#There are two types of function (1) Inbuilt Function  (2) Userdefined Function
#Ther are four types of function
# (1) No argument , No return value
# (2) Argument , No return value
# (3) No Argument , return value
# (4) Argument , Return value
# (1) No argument , No return value
#def addition():
#    a,b = map(int,input().split())
#    print(a+b)

#def main():
#    addition()
#if  __name__=='__main__':
#    main()

#(2)Argument , But no return Value
#def swap(a,b):
#    print(type(a),type(b))
#    temp = a[0]
#    a[0] = b[0]
#    b[0] = temp
#    print(a[0],b[0])

#def main():
#    a,b = map(int,input().split())
#    # when we pass value of a and b from main function the swap function does not affect on python.so,we have one way
    #to do it
    #Then we have to make a list
#    x=[0]*1
#    y=[0]*1
#    x[0]=a
#    y[0]=b
#    swap(x,y)
#    print(x[0],y[0])

#if __name__ == '__main__':
#    main()

#(3)
def main():
    x = fun()
    print(type(x))
#    x=addition()
#    #y=addition()
#    #print(x,y)

def fun():
#    return [1,2]
    return "Divy"


#def addition():
#    x,y = map(int,input().split())
#    print(x+y)

if __name__=='__main__':
    main()