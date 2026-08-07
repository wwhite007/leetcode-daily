# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 空树，高度为 0
        if root == None:
            return 0

        # 初始化队列和层次
        queue = [root]
        depth = 0

        # 当队列不为空
        while queue:
            # 当前层的节点数
            n = len(queue)
            # 弹出当前层的所有节点，并将所有子节点入队列
            for i in range(n):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        # 二叉树最大层次即为二叉树最深深度
        return depth
