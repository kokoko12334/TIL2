# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    
    def longestZigZag(self, root) -> int:

        stack = [[root,0,"all"]]

        answer = 0
        while stack:
            
            node,cnt,pre = stack.pop()
            answer = max(answer,cnt)
            if pre == "all":
                if node.left != None:
                    stack.append([node.left,cnt+1,"left"])
                if node.right != None:
                    stack.append([node.right,cnt+1,"right"])
            
            elif pre == "right":
                if node.left != None:
                    stack.append([node.left, cnt+1,"left"])
                if node.right != None:
                    stack.append([node.right, 1,"right"])

            elif pre == "left":
                if node.right != None:
                    stack.append([node.right, cnt+1,"right"])
                if node.left != None:
                    stack.append([node.left, 1,"left"])


        return answer