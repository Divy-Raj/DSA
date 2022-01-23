class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def addNode(self,node,data):
        if(node is None):
            return Node(data)
        if(data<node.data):
            node.left = self.addNode(node.left,data)
        else:
            node.right = self.addNode(node.right,data)

        return node

    def preOrder(self,node):
        if(node is None):
            return
        print(node.data,end=" ")
        self.preOrder(node.left)
        self.preOrder(node.right)

    def inOrder(self, node):
        if (node is None):
            return
        self.inOrder(node.left)
        print(node.data, end=" ")
        self.inOrder(node.right)
    def minValue(self,node):
        temp = node
        while(temp.left is not None):
            temp = temp.left
        return temp.data
    def maxValue(self,node):
        temp = node
        while(temp.right is not None):
            temp = temp.right
        return temp.data

def main():
    arr = list(map(int,input().split()))
    bst = BST()
    for ele in arr:
        bst.root = bst.addNode(bst.root,ele)
    bst.preOrder(bst.root)
    print()
    bst.inOrder(bst.root)
    print()
    print(bst.minValue(bst.root))
    print(bst.maxValue(bst.root))

if __name__=='__main__':
    main()