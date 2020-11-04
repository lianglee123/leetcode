from typing import *


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = 0
        self.char = ''
        self.children = [None] * 26


    def addWord(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not word:
            return
        node = self
        for c in word:
            index = ord(c) - ord('a')
            if self.children[index] is None:
                t = WordDictionary()
                t.char = c
                node.children[index] = t
            node = node.children[index]
        node.count += 1


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if not word: return self.count > 0
        return self.__search(self.children, word)

    def __search(self, nodes, word):
        char = word[0]
        if len(word) == 1:
            if char == '.':
                return any([n.count > 0 for n in nodes])
            else:
                index = ord(char) - ord("a")
                return nodes[index].char == char and nodes[index].count > 0
        else:
            if char == '.':
                for node in nodes:
                    if node and self.__search(node.children, word[1:]):
                        return True
                return False
            else:
                index = ord(char) - ord('a')
                return nodes[index] and nodes[index].char == char and self.__search(nodes[index], word[1:])



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

