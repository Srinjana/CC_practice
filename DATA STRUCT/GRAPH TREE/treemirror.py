# Python3 program to convert a binary
# tree to its mirror

class NewNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# """ Change a tree so that the roles of the
#     left and right pointers are swapped at
#     every node.
 
# So the tree...
#           4
#         /   \
#         2    5
#        / \
#       1   3
 
# is changed to...
#       4
#     /  \
#     5    2
#        /  \
#        3   1
# """
def mirror(node):
    if (node == None):
        return
    else:

        # temp = node

        # /* do the subtrees * /
        mirror(node.left)
        mirror(node.right)

        # swapping the pointers of left and right nodes

        node.left , node.right = node.right , node.left


# helper function for inorder traversal

def inorder(node):

    if (node == None):
        return

    inorder(node.left)
    print(node.data, end = " -- ")
    inorder(node.right)


# Driver code
if __name__ == "__main__":

    root = NewNode(4)
    root.left = NewNode(2)
    root.right = NewNode(5)
    root.left.left = NewNode(1)
    root.left.right = NewNode(3)

    # """ Print inorder traversal of
    #     the input tree """
    print("Inorder traversal of the constructed tree is")
    inorder(root)

    # """ Convert tree to its mirror """
    mirror(root)

    # """ Print inorder traversal of
    #     the mirror tree """
    print("\nInorder traversal of the mirror tree is ")
    inorder(root)


