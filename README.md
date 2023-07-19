# Nearest Number In BST

Implement a function that takes a Binary Search Tree (BST) and a target integer value as inputs. The function should find and return the value in the BST that is closest to the given target value. You can assume that there will be only one closest value.

Each node in the BST has an integer value, a left child node, and a right child node. A node is considered a valid BST node if it satisfies the following conditions: its value is strictly greater than the values of all nodes to its left, its value is less than or equal to the values of all nodes to its right, and its children nodes are either valid BST nodes themselves or null/None.

## Sample Input

```
tree =
             10
           /     \
          5      15
        /   \   /   \
       2     5 13   22
     /           \
    1            14
    target = 12
```

## Sample Output

13
