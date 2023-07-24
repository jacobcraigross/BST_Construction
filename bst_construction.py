'''
BST is a type of tree DS that also satisfies the BST property. 
The BST property says everything on the L side of the tree has to be smaller than the root (starting) node
and everything on the R side must be bigger. same rule applies to child nodes
so if you split the tree in half, one side bigger, one side smaller in values 
and if you split at the root ("master") node thats say 60, nothing on the R side can be say 44
and nothing on the left side can be say 77 same
again, same rule applies to the child nodes, they create their own little trees that can be split
keep everything nice and clean and 0(log n)

when talking about BST construction, we need three main methods. 
insert()
search()
delete()

TIME 
Big 0 --> avg case its balanced, you can div by 2 and its 0(log n)
worst case --> its unbalanced. straight branch down 10 -> 33 -> 67 -> 89 -> 126 its 0(n) linear

SPACE
if you implement recursively, its 0(log n) best case and 0(n) worst case. 
you have to store frames on the call stack, depending on the size of the tree

if you implement iteratively, you can get a 0(1) constant on both avg and worst. 
often iterative implementations are better from a space pov --> not adding frames to the call stack 
'''

# Each instance of this class represents a node in the tree. 
# The constructor initializes a new node with whatever given value and sets both the left and right children to None.

class BST:
    def __init__(self, value):
        self.value = value                                                                   # whatever value we pass in to start the tree off
        self.left = None                               # stubbing out the placeholder for the children, initially its None, so no children yet
        self.right = None     


               
    def insert(self, value):                                              # insertion method is called on the root node, then starts traversing
        currNode = self                     # currNode = self gets a ref to curr instance of the class. IOW: what node are we at? (keeps track)
        while True:                # cant use for loop cuz we dont know how big tree is for traversal. gotta create infinite loop until we break
            if value < currNode.value:
                if currNode.left is None:
                    currNode.left = BST(value)
                    break
                else:
                    currNode = currNode.left
            else:
                if currNode.right is None:
                    currNode.right = BST(value)
                    break
                else:
                    currNode = currNode.right
        return self                                                    

        
    def contains(self, value):
        while currNode is not None:
            if value < currNode.value:
                currNode = currNode.left
            elif value > currNode.value:
                currNode = currNode.right
            else:
                return True
        return False



    # remove() is a 2 step process      -->     1) find the node     2) actually remove it
    # and in remove() you want to keep track of the parent node for re-assignment purposes (so the tree doesnt collapse)
    def remove(self, value, parNode = None): 
        currNode = self
        while currNode is not None: # in this while loop is the easy work of finding the node
            if value < currNode.value:
                parNode = currNode
                currNode = currNode.left
            elif value > currNode.value:
                parNode = currNode
                currNode = currNode.right
            else: # from this else onward, we have found the node, now the hard work of removing it. (lots of edge cases)
                # 1st case, dealing with a node that has two kids. 
                if currNode.left is not None and currNode.right is not None:
                    currNode.value = currNode.right.getMinVal() # we will build this out below. 
