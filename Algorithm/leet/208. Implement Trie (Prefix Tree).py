

class Node:
    def __init__(self):
        self.end = False
        self.link={}

class Trie:

    def __init__(self):
        self.root = Node()
                
    def insert(self, word: str) -> None:
        
        cur = self.root
        for w in word:

            if w not in cur.link:
                cur.link[w] = Node()
            
            cur = cur.link[w]
        
        cur.end = True
            

    def search(self, word: str) -> bool:

        cur = self.root
        for w in word:

            if w in cur.link:
                cur = cur.link[w]
            else:
                return False
        
        if cur.end == False:
            return False
        
        return True
        

    def startsWith(self, prefix: str) -> bool:

        cur = self.root
        for w in prefix:

            if w in cur.link:
                cur = cur.link[w]
            else:
                return False

        return True
# class Node:
#     def __init__(self):
#         self.end = False # 마지막 문자열 여부, True면 마지막 문자열이다.
#         self.link={} #자식노드여부, 빈칸이면 자식노드가 없기 때문에 마지막 문자열이다.

# class Trie:

#     def __init__(self):
#         self.root = Node()   #root 노드를 만든다.
                
#     def insert(self, word: str) -> None:
        
#         cur = self.root #루트노드에서 시작한다.
#         for w in word:

#             if w not in cur.link:  #해당 문자열이 노드에 없다면
#                 cur.link[w] = Node() #새로운 노드를 연결하고
            
#             cur = cur.link[w] #새로 만든 노드로 이동한다.
        
#         cur.end = True  #마지막노드는 마지막 문자열이기 때문에 True로 바꾼다.
            

#     def search(self, word: str) -> bool:

#         cur = self.root #루트노드부터 시작해서
#         for w in word:

#             if w in cur.link:  # 해당 문자열이 존재하면
#                 cur = cur.link[w] #그 문자열 노드로 이동한다.
#             else:
#                 return False

#         return True
        

#     def delete(self, word: str) -> None:
#         self._delete_recursive(self.root, word, 0)

#     def _delete_recursive(self, node, word, index):
#         if index == len(word):
#             # 단어의 끝에 도달했을 때 해당 노드의 end 플래그를 False로 설정
#             if node.end:
#                 node.end = False
#             return

#         char = word[index]

#         if char in node.link:
#             # 다음 문자가 현재 노드에 존재하는 경우 재귀 호출
#             self._delete_recursive(node.link[char], word, index + 1)

#             # 삭제된 노드가 단말 노드이고 자식이 없으면 해당 노드 삭제
#             # 만약 ["app","apple"]이란 단어를 저장하고 "apple"을 삭제한다면 "app"은 삭제하면 안된고 "le"만 삭제해야 한다.=> node.linke[char].end == True인 경우
#             # 만약 ["banana",basic]이란 단어를 저장하고 basic을 삭제한다면 ba에서 -> [nana, sic] 으로 분기하기때문에 "banana"를 살리기 위해서 "sic"만 삭제되어야 한다.
#             #=> 이경우는 node.link[char].link != None인 경우
#             if not node.link[char].link and not node.link[char].end:
#                 del node.link[char]
#         else:
#             # Trie에 해당 문자열이 존재하지 않으면 삭제할 수 없음
#             return      


        
    

# a = Trie()

# a.insert("apple")
# a.insert("app")
# print(a.search("apple"))

# a.delete("apple")
# print(a.search("app"))