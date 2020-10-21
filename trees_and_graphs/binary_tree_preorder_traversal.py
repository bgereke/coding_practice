# Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
# Example 4:


# Input: root = [1,2]
# Output: [1,2]
# Example 5:


# Input: root = [1,null,2]
# Output: [1,2]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# iterative solution
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result
        stack = []
        while root or stack:
            if root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return result

# recursive version of solution
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def traverse(node, stack = [], result = []):
            if node:
                result.append(node.val)
                stack.append(node)
                node = node.left
                return traverse(node, stack, result)
            elif stack:
                node = stack.pop()
                node = node.right
                return traverse(node, stack, result)
            else:
                return result
        return traverse(root)

# one line recursive solution
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
            