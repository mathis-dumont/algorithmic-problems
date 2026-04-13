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
        def match(node,word):
            for i,c in enumerate(word):
                if c == '.':
                    for child in node.children.values():
                        if match(child,word[i+1:]):
                            return True
                    return False
                elif c not in node.children:
                    return False
                else:
                    node = node.children[c]
            return node.is_end
        return match(self.root,word)
        