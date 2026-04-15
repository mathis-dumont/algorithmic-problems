class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.is_end = True

    def search(self, word: str) -> bool:
        
        def map(word, node):
            for i,c in enumerate(word):
                if c != '.':
                    if c not in node.children:
                        return False
                    else:
                        node = node.children[c]
                else:
                    for child in node.children.values():
                        if map(word[i+1:], child):
                            return True
                    return False
            return node.is_end

        return map(word,self.root)
        
