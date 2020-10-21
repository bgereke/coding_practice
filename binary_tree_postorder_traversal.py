# Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [3,2,1]
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
# Output: [2,1]
 

# Constraints:

# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# iterative solution


# iterative solution
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result
        stack = [{'node': root, 'left': False, 'right': False}]
        while True:
            if stack[-1]['left'] is False and root.left is not None:  
                stack[-1]['left'] = True
                root = root.left
                stack.append({'node': root, 'left': False, 'right': False})
            elif stack[-1]['right'] is False and root.right is not None:
                stack[-1]['right'] = True
                root = root.right  
                stack.append({'node': root, 'left': False, 'right': False})
            elif stack:
                result.append(root.val) 
                stack.pop()
                if not stack:
                    return result
                else:
                    root = stack[-1]['node']

# one line recursive solution
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]