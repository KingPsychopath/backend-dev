# Tree traversal in Python
class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


def inorder(root):
    if root:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse right
        inorder(root.right)


def postorder(root):

    if root:
        # Traverse left
        postorder(root.left)
        # Traverse right
        postorder(root.right)
        # Traverse root
        print(str(root.val) + "->", end='')


def preorder(root):

    if root:
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)

# Iterative Implementation of tree traversal
def preorder2(root):
    if root is None:    # if the root is None, return an empty list
        return []
    stack = [root]    # create an empty stack and add the root to it
    result = []    # create an empty list to store the result
    while stack:    # while there are still nodes to process
        curr = stack.pop()        # pop the top node from the stack
        result.append(curr.val)        # add the node's value to the result list
        if curr.right:        # add the node's right child to the stack (if it exists)
            stack.append(curr.right)
        if curr.left:        # add the node's left child to the stack (if it exists)
            stack.append(curr.left)
    return result    # return the result list

def inorder2(root):
    if root is None:
        return []
    stack = [] # create an empty stack
    result = [] # create an empty list to store the result
    while stack or root: # while there are still nodes to process
        if root: # if there is a left child, add it to the stack and move to the left child
            stack.append(root)
            root = root.left
        else: # if there is no left child, pop the top node from the stack, add its value to the result list, and move to the right child
            curr = stack.pop()
            result.append(curr.val)
            root = curr.right
    return result # return the result list

def postorder2(root):
    if root is None:    # If the root is None, return an empty list
        return []
    
    stack = [root]    # Create a stack to keep track of nodes
    result = []    # Create a list to store the result

    while stack:    # While there are still nodes in the stack
        curr = stack.pop()        # Pop the top node from the stack
        result.append(curr.val)        # Add the node's value to the result list

        if curr.left:        # Add the node's children to the stack
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    return result[::-1]    # Return the result list in reverse order to get the postorder traversal



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal Recursive")
inorder(root)
print("\nInorder traversal Iterative ")
print(inorder2(root))

print("\nPreorder traversal Recursive")
preorder(root)
print("\nPreorder traversal Iterative")
print(preorder2(root))


print("\nPostorder traversal Recursive ")
postorder(root)
print("\nPostorder traversal Iterative")
print(postorder2(root))