import random

class BinaryTree:
    parent = None
    left = None
    right = None
    value = None

    def __init__(self, parentBranch = None):
        self.parent = parentBranch

    def addValue(self, val):
        if self.value == None:
            self.value = val
        elif val < self.value:
            if not self.left:
                self.left = BinaryTree(self)
            self.left.addValue(val)
        else:
            if not self.right:
                self.right = BinaryTree(self)
            self.right.addValue(val)

def treeSort(arr):
    tree = BinaryTree()
    #complete tree
    for val in arr:
        tree.addValue(val)

    sortedArr = []

    #run into tree
    currentBranch = tree
    while currentBranch:
        if(currentBranch.left and (currentBranch.left.value != None) ):
            currentBranch = currentBranch.left
            continue
        if(currentBranch.value != None):
            sortedArr.append(currentBranch.value)
            currentBranch.value = None
            if(currentBranch.right):
                currentBranch = currentBranch.right
            else:
                currentBranch = currentBranch.parent
            continue
        currentBranch = currentBranch.parent

    return sortedArr

def createRandomArray(length):
    arr = []
    for i in range(length):
        arr.append(random.randint(0, length))
    return arr

arr1 = createRandomArray(1000)
print(str(arr1))
arr2 = treeSort(arr1)
print(str(arr2))