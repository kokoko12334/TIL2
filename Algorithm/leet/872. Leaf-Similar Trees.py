# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def dfs(self, root):
        stack = [root]
        arr = []
        while stack:
            node = stack.pop()
            
            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)
            if node.left == None and node.right == None:
                
                arr.append(node.val)

        return arr

    def leafSimilar(self, root1, root2) -> bool:
        

        arr1 = self.dfs(root1)
        arr2 = self.dfs(root2)

        l_1 = len(arr1)
        l_2 = len(arr2)

        answer = True

        if l_1 == l_2:
            for i in range(l_1):

                if arr1[i] != arr2[i]:
                  
                    answer = False
                    break

        else:
            answer = False

        return answer