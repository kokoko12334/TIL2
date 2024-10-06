# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def searchBST(self, root, val: int):
        

        if root != None:
            stack = [root]
            answer = None
            while stack:

                node = stack.pop()

                
                if val < node.val and node.left != None:
                    stack.append(node.left)
                elif val > node.val and node.right != None:
                    stack.append(node.right)
                elif val == node.val:
                    answer = node
                    break
            
            return answer

        else:
            return None