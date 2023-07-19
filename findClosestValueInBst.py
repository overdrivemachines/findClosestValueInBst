def findClosestValueInBst(tree, target):
    node = tree
    current_value = node.value
    closest_value = current_value
    least_diff = abs(current_value - target)

    print("target:", target)

    while node:
        current_diff = abs(target - node.value)
        print(node.value, ":", current_diff)
        if current_diff < least_diff:
            closest_value = node.value
            least_diff = current_diff

        # left_diff = current_diff + 1
        # right_diff = current_diff + 1
        if node.value < target:
            node = node.left
        else:
            node = node.right

    return closest_value




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
