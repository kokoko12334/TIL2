# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root):
        
        if root != None:
            queue = deque()
            queue.append([root,0])
            answer = {k: [] for k in range(101)}
            while queue:
                node,rank = queue.popleft()
                answer[rank].append(node.val)

                if node.left != None:
                    queue.append([node.left,rank+1])
                if node.right != None:
                    queue.append([node.right,rank+1])

            result = []

            for v in answer.values():
                if v:
                    result.append(v[-1])

            return result

        else:
            return None