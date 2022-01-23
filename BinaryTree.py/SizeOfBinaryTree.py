class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def preOrderTraversal(root):
    if(root is None):
        return
    print(root.data,end=" ")
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)

def sizeOfBT(root):

    if(root is None):
        return 0
    return sizeOfBT(root.left)+sizeOfBT(root.right)+1
    # or use below code
    #lside = sizeOfBT(root.left)
    #rside = sizeOfBT(root.right)
    #return lside + rside +1

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)
    root.left.left.right.left = Node(9)

    print(sizeOfBT(root))

if __name__=='__main__':
    main()
