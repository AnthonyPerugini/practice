# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def find_lineage(node, target):
            ancestors = []

            while node != target:
                target_ancestors.append(node)

                if node.val > target.val:
                    node = node.left
                elif node.val < target.val:
                    node = node.right

            ancestors.append(target)
            return ancestors

        p_lineage = find_lineage(root, p)
        q_lineage = set(find_lineage(root, q))

        for ancestor in p_lineage[::-1]:
            if ancestor in q_lineage:
                return ancestor

        return False

            








