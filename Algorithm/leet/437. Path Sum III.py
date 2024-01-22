# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum: int) -> int:
        
        
        if root != None:
            stack = [[root,[]]]
            answer = 0
            while stack:

                node, arr = stack.pop()
                new_arr = []

                for i in arr:

                    new = node.val + i
                    if new == targetSum:
                        answer += 1
                    new_arr.append(new)            
                
                if node.val == targetSum:
                    answer += 1
                new_arr.append(node.val)

                if node.left != None:
                    stack.append([node.left,new_arr])

                if node.right != None:
                    stack.append([node.right,new_arr])




            return answer
        else:
            return 0