class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def isBst(node,minRange,maxRange):
    if(node is None):
        return True
    if(node.data<minRange or node.data>maxRange):
        return False
    return isBst(node.left,minRange,node.data) and isBst(node.right,node.data,maxRange)


def main():
    root = Node(50)
    root.left = Node(25)
    root.right = Node(75)
    root.left.left = Node(15)
    root.left.right = Node(30)
    root.right.left = Node(70)
    root.right.right = Node(85)
    root.left.left.left = Node(10)
    root.left.left.right = Node(23)

    if(isBst(root,float('-inf'),float('inf'))):
        print("BT is BST")
    else:
        print("BT is not BST")

if __name__=='__main__':
    main()
