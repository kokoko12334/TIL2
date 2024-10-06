


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> 'TreeNode':
        

        ancestor = {}
        
        stack = [[root,[]]]


        while stack:

            node, lst = stack.pop()
            
            lst.append(node.val)
            ancestor[node.val] = lst[:]

            if node.left != None:
                stack.append([node.left,lst[:]])
            if node.right != None:
                stack.append([node.right,lst[:]])

        

        a_p = ancestor[p.val]

        a_q = ancestor[q.val]

        np = len(a_p)
        nq = len(a_q)

        if np > nq:
            dif = np -nq
            for _ in range(dif):
                a_q.append("")
        else:
            dif = nq - np
            for _ in range(dif):
                a_p.append("")

        idx = len(a_q) - 1
        
        
        while idx >= 0:
            if a_p[idx]== a_q[idx]:
                break 
            
            idx -= 1

        answer = a_q[idx]

        stack = [root]
        answer_node = TreeNode(1)
        while stack:
            node = stack.pop()
            if answer == node.val:
                answer_node = node
            if node.left != None:
                stack.append(node.left)
            if node.right != None:
                stack.append(node.right)

        return answer_node