# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    possible_paths = []

    def pathSum(self, root: TreeNode, targetSum: int, current_path=None) -> List[List[int]]:

        if root is None:
            return []

        if current_path is None:
            current_path = []

        cur_node = root

        while cur_node



