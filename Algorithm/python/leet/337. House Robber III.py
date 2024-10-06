# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        dp = defaultdict(int)
        def dfs(node):

            if node == None:
                return 0

            if dp[node]:
                return dp[node]
            
            val = 0

            if node.left != None:
                val += dfs(node.left.left) + dfs(node.left.right)
            
            if node.right != None:
                val += dfs(node.right.left) + dfs(node.right.right)

            result = max( val + node.val, dfs(node.left) + dfs(node.right))
            dp[node] = result
            
            return result
        
        answer = dfs(root)
        # print(dp)
        return answer