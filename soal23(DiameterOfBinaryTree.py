# https://leetcode.com/problems/diameter-of-binary-tree/
# https://www.interviewbit.com/blog/diameter-of-a-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getDepth(self, root):
        if not root:
            return 0
        leftSubtreeDepth = self.getDepth(root.left)
        rightSubtreeDepth = self.getDepth(root.right)
        return max(leftSubtreeDepth, rightSubtreeDepth) + 1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0;
        leftSubtreeDiameter = self.diameterOfBinaryTree(root.left);
        rightSubtreeDiameter = self.diameterOfBinaryTree(root.right);
        diameter = self.getDepth(root.left) + self.getDepth(root.right);
        diameter = max(diameter, max(leftSubtreeDiameter, rightSubtreeDiameter));
        return diameter;