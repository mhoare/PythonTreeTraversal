class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def preOrder(self):
        returnList = [self.data]
        if self.left:
            returnList = returnList + self.left.preOrder()
        if self.right:
            returnList = returnList + self.right.preOrder()
        return returnList

    def postOrder(self):
        returnList = []
        if self.left:
            returnList = returnList + self.left.postOrder()
        if self.right:
            returnList = returnList + self.right.postOrder()
        return returnList + [self.data]

    def inOrder(self):
        returnList = []
        if self.left:
            returnList = returnList + self.left.inOrder()
        returnList = returnList + [self.data]
        if self.right:
            returnList = returnList + self.right.inOrder()
        return returnList

    def binarySearch(self, element):
        print self.preOrder()
        # Will tell whether an element is in the tree or not
        if (self.data == element):
            return True
        if (element > self.data and self.right):
            return self.right.binarySearch(element)
        if (element < self.data and self.left):
            return self.left.binarySearch(element)
        return False

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
print(tree.preOrder())
print "\nIn Order:"
print(tree.inOrder())
print "\nPost Order:"
print(tree.postOrder())
print('''
Binary Search for number 3 in tree above
(result will be true if element found and false if not)
''')
print(tree.binarySearch(3))
print '''
Binary Search for number 9 in tree above
(result will be true if element found and false if not)
'''
print(tree.binarySearch(9))
