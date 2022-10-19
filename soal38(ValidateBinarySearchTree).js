// https://leetcode.com/problems/validate-binary-search-tree/
// https://alkeshghorpade.me/post/leetcode-validate-binary-search-tree


/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function(root) {
    if (!root) {
        return true;
    }

    return checkValidBST(root);
};

var checkValidBST = function(root, min = -Infinity, max = +Infinity) {
    if (!root) {
        return true;
    }

    if (root.val <= min || root.val >= max) {
        return false;
    }

    return checkValidBST(root.left, min, root.val) && checkValidBST(root.right, root.val, max);
}