# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root) -> int:

        results = [0]*10000


        stack = [[root,0]]
        depth = 0
        while stack:
            node, rank = stack.pop()
            depth = max(depth,rank)
            results[rank] += node.val

            if node.left != None:
                stack.append([node.left,rank+1])
            if node.right != None:
                stack.append([node.right,rank+1])
        results = results[:depth+1]
        
        answer = max(range(len(results)), key=lambda x : results[x])
        
        return answer + 1