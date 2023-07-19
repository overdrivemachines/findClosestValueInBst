def findClosestValueInBst(tree, target):
    node = tree
    result = node.value
    least_diff = abs(node.value - target)

    while node:
        current_diff = abs(target - node.value)

        # if target is found in the BST, return it
        if current_diff == 0:
            return target

        # updating result if the current difference is less than the least difference
        if current_diff < least_diff:
            least_diff = current_diff
            result = node.value

        # if the current node doesn't have any children, return result
        if node.left == None and node.right == None:
            return result

        # if target is less than the node's value, move to the left,
        # otherwise move to the right
        if node.left != None and target < node.value:
            node = node.left
        elif node.right != None:
            node = node.right
        else:
            return result
    return result


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# tree =
#              10
#            /     \
#           5b      15
#         /   \    /   \
#        2     5a 13   22
#      /           \
#     1            14
#     target = 12

# Level 3:
one = BST(1)
fourteen = BST(14)

# Level 2:
two = BST(2)
two.left = one
five_a = BST(5)
thirteen = BST(13)
thirteen.right = fourteen
twentytwo = BST(22)

# Level 1:
five_b = BST(5)
five_b.left = two
five_b.right = five_a
fifteen = BST(15)
fifteen.left = thirteen
fifteen.right = twentytwo

# Level 0:
ten = BST(10)
ten.left = five_b
ten.right = fifteen

print(findClosestValueInBst(ten, 12))
