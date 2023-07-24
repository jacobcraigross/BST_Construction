# Each instance of this class represents a node in the tree. 
# The constructor initializes a new node with whatever given value and sets both the left and right children to None.
class BST:
    def __init__(self, value):
        self.value = value # whatever value we pass in to start the tree off
        self.left_child = None # stubbing out the placeholder for the children, initially its None, so no children yet
        self.right_child = None     
     
    def insert(self, value): # insertion method is called on the root node, then starts traversing
        currrent_node = self # curr node = self gets a ref to curr instance of the class. IOW: what node are we at? (keeps track)
        while True: # cant use for loop cuz we dont know how big tree is for traversal. gotta create infinite loop until we break
            if value < current_node.value:
                if current_node.left_child is None:
                    current_node.left_child = BST(value)
                    break
                else:
                    current_node = current_node.left_child
            else:
                if current_node.right_child is None:
                    current_node.right_child = BST(value)
                    break
                else:
                    current_node = current_node.right_child
        return self                                                    

    def contains(self, value):
        while current_node is not None:
            if value < current_node.value:
                current_node = current_node.left_child
            elif value > current_node.value:
                current_node = current_node.right_child
            else:
                return True
        return False

    # remove() is a 2 step process - 1) find the node - 2) actually remove it
    # and in remove() you want to keep track of the parent node for re-assignment purposes (so the tree doesnt collapse)
    def remove(self, value, parent_node = None): 
        current_node = self
        while current_node is not None: # in this while loop is the easy work of finding the node
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left_child
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right_child
            else: # from this else onward, we have found the node, now the hard work of removing it. (lots of edge cases)
                # 1st case, dealing with a node that has two kids. 
                if current_node.left_child is not None and current_node.right_child is not None:
                    current_node.value = current_node.right_child.get_min_val() # we will build this out below. 
                    current_node.right_child.remove(current_node.value, curr_node)
                # 2nd case is if we dont have 2 children present (2 sub cases within that)
                elif parent_node is None:
                    if current_node.left_child is not None:
                        current_node.value = current_node.left.value
                        current_node.right_child = current_node.left_child.right_child
                        current_node.left_child = current_node.left_child.left_child
                    elif current_node.right_child is not None:
                        current_node.value = current_node.right_child.value
                        current_node.left_child = current_node.right_child.left_child
                        current_node.right_child = current_node.right_child.right_child
                    else:
                        current_node.value = None
                # so if were NOT dealing with the root node
                # if this node has either 1 or 0 children, is the currNode a L or R child?
                elif parent_node.left_child == current_node: # if its a L child 
                    parent_node.left_child = currNode.left_child if current_node.left_child is not None else current_node.right_child
                elif parent_node.right_child == current_node:
                    parent_node.right_child = current_node.left_child if current_node.left_child is not None else current_node.right_child
                break
        return self

    def get_min_val(self):
        current_node = self
        while current_node.left_child is not None:
            current_node = current_node.left_child
        return current_node.value
