__author__ = 'alfmunny'

'''

Question:

Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root):
        res = []
        if root is None:
            return res

        tree = [[root]]
        res.append([root.val])
        itree = 1
        while True:
            temp = []
            temp_val = []
            for node in tree[itree-1]:
                if node.left is not None:
                    temp.append(node.left)
                    temp_val.append(node.left.val)
                if node.right is not None:
                    temp.append(node.right)
                    temp_val.append(node.right.val)
            if len(temp) == 0:
                break
            else:
                tree.append(temp)
                res.append(temp_val)
            itree += 1

        res.reverse()

        return res

