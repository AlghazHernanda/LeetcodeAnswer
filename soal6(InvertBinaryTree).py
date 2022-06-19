# https://leetcode.com/problems/invert-binary-tree/submissions/


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.helper(root)
        return root
    def helper(self, node):
        if not node:
            return
        node.left, node.right = node.right, node.left
        self.helper(node.left)
        self.helper(node.right)