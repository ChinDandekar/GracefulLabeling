#!/usr/bin/env python
# coding: utf-8

# In[255]:


from random import randint
from math import factorial


# In[256]:




# In[257]:


#this is the Node class, which stores the value
#of the node, and the left child, right child and parent nodes

class Node:
    def __init__(self, value, left, right, parent):  #constructor
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
    def nodePrint(self):                             #prints the value of the node
        print(self.value, end = '')
        
    def setRight(self,right):                        #sets the right child of the node
        self.right = right
    
    def setLeft(self,left):                          #sets left child of the node
        self.left = left
        
    def setParent(parent):                           #sets the parent of the node
        self.parent = parent

# The Label class, which stores the edge values of the binary tree.
# Since we exclusively are dealing with binary trees, storing the 
#"parent" and "child" nodes in the label class is useful to find out
# where in the tree there are repeating edge values (if a tree is not graceful)
class Label:
    def __init__(self, difference, parentNode, childNode):     #constructor
        self.difference = difference
        self.parentNode = parentNode
        self.childNode = childNode


# In[258]:


class BinaryTree:
        
    def __init__(self, nodeArray, isPrintFail):        #constructor
        self.allLabelings = []
        self.nodeArray = nodeArray                     #the array that will be converted to a binary tree
        self.isGraceful = True                         #stores whether the tree is graceful
        self.isPrintFail = isPrintFail                 #stores whether or not to print the tree in case its not graceful
    
    def setRoot(self,root):
        self.root = root
        
    def printAllLabelings(self):                        #prints each edge value, its "parent" and its "child"
        for x in range(0,len(self.allLabelings)):
            label = self.allLabelings[x]
            print("Value = " + str(label.difference) + "; Parent = " + str(label.parentNode.value), end = ' ')
            print("; Child = " + str(label.childNode.value))

    def isInLabels(self,diff):                         #searches through the array of labels to see if there already
                                                       #exists another label with the value diff
        for x in range(0,len(self.allLabelings)):
            if(diff == self.allLabelings[x].difference):
                return True
        return False
    
    def checkAndPrintLabel(self, label):                #calls isInLabels to check if given label value already exists
                                                        #in the tree, if it does then prints the current tree out and
                                                        #sets isGraceful to false, otherwise adds label to allLabelings
        if((self.isInLabels(label.difference))):
            if(self.isPrintFail):
                self.allLabelings.append(label)
                print("Not a graceful labeling, edge value " + str(label.difference) + " repeated")
                self.printAllLabelings()
            self.isGraceful = False
        else:
            self.allLabelings.append(label)
        
        
    def nodeArrayToBST(self, start, end):            #recursively constructs a binary tree from nodeArray
        
        arr = self.nodeArray
        # Base Case
        if (start > end): 
            return None 

        # Get the middle element and make it root 
        mid = (int)((start + end)/2)
        curNode = Node(arr[mid],None,None,None)

        # Recursively construct the left subtree 
        # and make it left child of curNode
        # Then constructs a label between curNode and left child
        # and calls checkAndPrintLabel
        curNode.setLeft(self.nodeArrayToBST( start, mid - 1)) 
        if(self.isGraceful and curNode.left != None):        
            label = Label(abs(curNode.value - curNode.left.value),curNode, curNode.left)    
            self.checkAndPrintLabel(label)

        # Recursively construct the right subtree 
        # and make it right child of curNode
        # Then constructs a label between curNode and right child
        # and calls checkAndPrintLabel
        curNode.setRight(self.nodeArrayToBST(mid + 1, end)) 
        if(self.isGraceful and curNode.right != None):
            label = Label(abs(curNode.value - curNode.right.value),curNode, curNode.right)
            self.checkAndPrintLabel(label)

        return curNode
    
        
    def printHorizontally(self, root, space):                            #recursively prints the tree horizontally
        COUNT = 10
        # Base case
        if (root == None) :
            return

        # Increase distance between levels
        space += COUNT

        # Process right child first
        self.printHorizontally(root.right, space)

        # Print current node after space
        # count
        print()
        for i in range(COUNT, space):
            print(end = " ")
        print(root.value)

        # Process left child
        self.printHorizontally(root.left, space)
        
    def printTree(self,root):                                #prints the tree, and information about graceful 
                                                             #labeling of the tree
        if(self.isGraceful):
            print("Congratulations, your labeling of ", end = '')
            print(self.nodeArray, end = ' ')
            print(" is graceful")
        if(self.isPrintFail):
            self.printHorizontally(root,0)


# In[259]:


#example of tree that is not gracefully labeled
notes = [0,1,2,3,4,5,6]
bt = BinaryTree(notes, True)
bt.setRoot(bt.nodeArrayToBST(0, len(bt.nodeArray)-1))
bt.printTree(bt.root)


#example of tree that is gracefully labeled
notes = [6, 1, 3, 4, 0, 5, 2]
bt = BinaryTree(notes, True)
bt.setRoot(bt.nodeArrayToBST(0, len(bt.nodeArray)-1))
bt.printTree(bt.root)


# In[263]:


def heapPermute(size, tree):                        #uses Heap's algorithm to compute every tree of level n
                                                              #and prints every tree that is graceful
    # Base case, if size is 1, the permutation
    # is complete, and checks and prints the graceful tree
    if size == 1:
        bTree = BinaryTree(tree, False)
        bTree.setRoot(bTree.nodeArrayToBST(0,len(bTree.nodeArray)-1))
        bTree.printTree(bTree.root)
        return
     
    # Recursive case
    for i in range(size):
        heapPermute(size-1, tree)
 
        # if size is odd, swap 0th i.e (first)
        # and (size-1)th i.e (last) element
        # else If size is even, swap ith
        # and (size-1)th i.e (last) element
        if size%2 == 1:
            temp = tree[0]
            tree[0] = tree[size-1]
            tree[size-1] = temp
        else:
            temp = tree[i]
            tree[i] = tree[size-1]
            tree[size-1] = temp
 
    
def bruteForce(n):                            #driver code that calls the heapPermute method, n refers to the 
                                              #number of levels in the tree
    size = (2**n) - 1
    tree2 = []
    for y in range(0,size):    
        tree2.append(y)
    heapPermute(size, tree2)


# In[264]:


#this is a very very very computationally heavy method, O((2^n)!*2^n), due to the number of possible permutations.


bruteForce(3)


# In[275]:


def fillIn(array, n):                                #takes an unfinished array and fills it randomly till it is of
                                                     #size 2^n - 1
    arr = array.copy()
    while(len(arr) < (2**n)-1):
        x = randint(0,(2**(n)-2))
        if(arr.count(x) == 0):
            arr.append(x)
    return arr

def checkIfIndex(arr2D, x):                          #given a 2D array that contains a number and the index, and
                                                     #an index, checks if the index is present in the 2D array
    for y in range(0, len(arr2D)):
        if(arr2D[y][1] == x):
            return arr2D[y][0]
    return -1
def fillInSides(arr2D,n):                            #given a 2D array that contains a number and the index for each
                                                     #user-inputted number wanted in the array, randomly fills in the
                                                     #rest of the array of size 2**n - 1
    arr = []
    for x in range(0,(2**n)-1):
        arr.insert(x,checkIfIndex(arr2D, x))
    for y in range(0,len(arr)):
        if(arr[y] == -1):
            isInserted = False
            while(not isInserted):
                x = randint(0,(2**(n)-2))
                if(arr.count(x) == 0):
                    arr[y] = x
                    isInserted = True
    return arr


# In[285]:


incArr = [[0,0],[6,1],[7,3]]
print(fillInSides(incArr,3))


# In[295]:


def finishGracefulGraph(arr, n):                #uses fillInSides() to create arrays, and checks if they are
                                                       #graceful, stops at 100,000 computations
    foundGraceful = False
    counter = 0
    while(not foundGraceful):
        newArr = fillInSides(arr, n)
        bTwee = BinaryTree(newArr, False)
        bTwee.setRoot(bTwee.nodeArrayToBST(0, len(bTwee.nodeArray)-1))
        foundGraceful = bTwee.isGraceful
        bTwee.printTree(bTwee.root)
        counter = counter+1
        if(counter > 100000):
            print("Could not find a graceful labeling after 100,000 computations")
            return


# In[307]:


twee = [[0,3],[6,1],[3,5]]
finishGracefulGraph(twee, 3)


# In[ ]:




