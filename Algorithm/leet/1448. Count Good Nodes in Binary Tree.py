


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        stack = [[root,-10001]]

        answer = 0
        while stack:
            node, max_value = stack.pop()


            if node.val >= max_value:
                answer += 1
                max_value = node.val

            if node.left != None:
                stack.append([node.left, max_value])
            
            if node.right != None:
                stack.append([node.right, max_value])


        return answer