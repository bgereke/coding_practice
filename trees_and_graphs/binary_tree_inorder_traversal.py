# Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
# Example 4:


# Input: root = [1,2]
# Output: [2,1]
# Example 5:


# Input: root = [1,null,2]
# Output: [1,2]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# iterative solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result
        stack = []
        while True:
            if root.left is not None:
                stack.append(root)
                root = root.left
            else:
                result.append(root.val)
                if root.right is not None:
                    root = root.right
                elif stack:
                    root = stack.pop()
                    root.left = None
                else:
                    return result

# recursive solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def traverse(node, stack = [], result = []):
            if node.left is not None:
                stack.append(node)
                node = node.left
                return traverse(node, stack, result)
            else:
                result.append(node.val)
                if node.right is not None:
                    node = node.right
                    return traverse(node, stack, result)
                elif stack:
                    node = stack.pop()
                    node.left = None
                    return traverse(node, stack, result)
                else:
                    return result
        if root:
            return traverse(root)
        else:
            return []