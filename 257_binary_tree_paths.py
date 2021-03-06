# 257. Binary Tree Paths
#
# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        result, path = [], []
        self.binaryTreePathsRecu(root, path, result)
        return result

    def binaryTreePathsRecu(self, node, path, result):
        if node is None:
            return

        if node.left is node.right is None:
            ans = ""
            for n in path:
                ans += str(n.val) + "->"
            result.append(ans + str(node.val))

        if node.left:
            path.append(node)
            self.binaryTreePathsRecu(node.left, path, result)
            path.pop()

        if node.right:
            path.append(node)
            self.binaryTreePathsRecu(node.right, path, result)
            path.pop()


# https://gengwg.blogspot.com/2018/03/leetcode-257-binary-tree-paths.html
class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        res = []
        if root is None:
            return res
        self.helper(root, '', res)
        return res

    def helper(self, node, path, result):
        # if node is None:    # recursion stop condition
        #    return
        if node.left is node.right is None: # leaf node
            result.append(path + str(node.val)) # append current found path
        if node.left:
            self.helper(node.left, path + str(node.val) + '->', result)
        if node.right:
            self.helper(node.right, path + str(node.val) + '->', result)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.left.left = TreeNode(4)
    print Solution().binaryTreePaths(root)
