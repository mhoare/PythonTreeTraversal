class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def preOrder(self):
        print(self.data)
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print self.data

    def inOrder(self):
        if self.left:
            self.left.inOrder()
        print self.data
        if self.right:
            self.right.inOrder()


def arrayToTree(array):
    length = len(array)
    if length == 0:
        return
    elif length == 1:
        return Tree(array[0])
    if (length % 2 == 0):
        # Even number
        middle = (length / 2) - 1
    else:
        middle = ((length + 1) / 2) - 1
    tree = Tree(array[middle], arrayToTree(array[0:middle]), arrayToTree(array[middle+1:]))
    return tree

tree = arrayToTree([1,2,3,4,5,6,7])

print """
***** EXAMPLE *****
List: [1,2,3,4,5,6,7]
Tree: 
            4
    2               6
1       3       5       7
"""

print "Pre Order:"
tree.preOrder()
print "\nIn Order:"
tree.inOrder()
print "\nPost Order:"
tree.postOrder()
