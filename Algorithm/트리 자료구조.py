#루트 노드 : 최상위 노드
#단말노드: 자식이 없는 노드
#크기: 트리에 포함된 모든 노드의 개수(루트노드의 깊이는 0임.)
#깊이: 루트 노드부터의 거리
#높이: 깊이 중 최댓값
#차수: 각 노도의 간선 개수(선분 갯수)
#참고로 크기가 n이면 전체 간선의 갯수는 n-1이다

#순회 방법
#bfs(Breath First Search) 큐로 가능
#계층중심으로 이루어짐
#DFS(Depth First Search)  스택으로 가능

#중위 순회(Inorder): Root를 중간에 순회(left->root->right)
#전위 순회(Preorder): Root를 제일 먼저(root->left-> right)
#후위 순회(Postorder): Root를 제일 나중에 순회(left->right->root)



class Treenode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Binary_search_tree():
    def __init__(self):
        self.root = None



bst1 = Treenode(10)
bst2 = Treenode(20)
bst3 = Treenode(30)
bst4 = Treenode(40)
bst5 = Treenode(50)
bst6 = Treenode(60)
bst7 = Treenode(70)



tree = Binary_search_tree()




























