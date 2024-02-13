class Node:
    def __init__(self):
        self.end = False 
        self.data = None
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
            if cur.data == None:
                cur.data = w
        
        cur.end = True  

    def search(self, word: str):

        cur = self.root 
        for w in word:

            if w in cur.link:  
                cur = cur.link[w] 
            else:
                return None

        return cur
    
    def dfs(self,word):

        node = self.search(word)

        if node == None:
            return []
        
        stack = [[node,word[:-1]]]
        arr = []
        while stack:
            node,w = stack.pop()

            if node.data != None:
                w += node.data

            if node.end == True:
                arr.append(w)
                

            for i in node.link.values():
                stack.append([i,w])
        
        arr = sorted(arr)[:3]
        
        return arr

   
class Solution:
    def suggestedProducts(self, products, searchWord: str):

        trie = Trie()
        for p in products:
            trie.insert(p)
        
        answer = []
        word = ""
        for w in searchWord:
            word += w
            
            result = trie.dfs(word)
            answer.append(result)

        return answer