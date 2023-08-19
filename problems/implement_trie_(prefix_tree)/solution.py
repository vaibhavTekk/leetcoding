class Trie:

    def __init__(self):
        self.children = [None]*26
        self.terminal = False

    def insert(self, word: str) -> None:
        if word:
            ind = ord(word[0]) - ord('a')
            if self.children[ind]:
                self.children[ind].insert(word[1:])
            else:
                newnode = Trie()
                self.children[ind] = newnode
                self.children[ind].insert(word[1:])
        else:
            self.terminal = True

    def search(self, word: str) -> bool:
        if word:
            ind = ord(word[0]) - ord('a')
            if self.children[ind]:
                return self.children[ind].search(word[1:])
            else:
                return False
        else:
            return self.terminal
     

    def startsWith(self, prefix: str) -> bool:
        if prefix:
            ind = ord(prefix[0]) - ord('a')
            if self.children[ind]:
                return self.children[ind].startsWith(prefix[1:])
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)