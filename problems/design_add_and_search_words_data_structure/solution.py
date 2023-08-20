class WordDictionary:
    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word: str) -> None:
        if word:
            curr = word[0]
            if curr not in self.children:
                self.children[curr] = WordDictionary()
            self.children[curr].addWord(word[1:])
            return
        else:
            self.end = True
            
    def search(self, word: str) -> bool:
        if word:
            curr = word[0]
            if curr == '.':
                for i in self.children:
                    if self.children[i].search(word[1:]):
                        return True
                return False
            else:
                if curr not in self.children:
                    return False
                return self.children[curr].search(word[1:])
        return self.end
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)