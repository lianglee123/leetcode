from typing import *




class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = 0
        self.char = ''
        self.children = [None] * 26


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not word:
            return
        node = self
        for c in word:
            index = ord(c) - ord('a')
            if self.children[index] is None:
                t = Trie()
                t.char = c
                node.children[index] = t
            node = node.children[index]
        node.count += 1


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        for c in word:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                return False
            node = node.children[index]
        return node.count > 0


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        for c in prefix:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                return False
            node = node.children[index]
        return node is not None



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
if __name__ == '__main__':
    obj = Trie()
    word = "hello"
    prefix = "he"
    obj.insert("apple")
    obj.insert("hello")
    param_2 = obj.search(word)
    param_3 = obj.startsWith(prefix)
    print(param_2, param_3, obj.startsWith("bi"), obj.search("cc"))

    ["Trie","insert","search","search","startsWith","insert","search"]
[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]

["Trie","insert","search","search","startsWith","insert","search"]
[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]