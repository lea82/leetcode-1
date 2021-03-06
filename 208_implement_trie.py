# Implement a trie with insert, search, and startsWith methods.
#
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
#
# http://bookshadow.com/weblog/2015/05/08/leetcode-implement-trie-prefix-tree/

class TrieNode(object):
    def __init__(self):
        self.children = dict()
        self.isWord = False


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word:
            child = node.children.get(letter)
            if child is None:
                child = TrieNode()
                node.children[letter] = child
            node = child
        node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for letter in word:
            node = node.children.get(letter)
            if node is None:
                return False
        return node.isWord

    # iterative dfs
    def search(self, word):
        return self.find(self.root, word)

    def find(self, node, word):
        if word == '':
            return node.isWord
        else:
            child = node.children.get(word[0])
            if child:
                return self.find(child, word[1:])
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for letter in prefix:
            node = node.children.get(letter)
            if node is None:
                return False
        return True

# https://gengwg.blogspot.com/2018/05/leetcode-208-implement-trie-prefix-tree.html
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        p = self.root
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
        p['#'] = True

    def search(self, word):
        node = self.find(word)
        return node is not None and '#' in node

    def startsWith(self, prefix):
        return self.find(prefix) is not None

    def find(self, w):
        p = self.root
        for c in w:
            if c not in p:
                return None
            p = p[c]
        return p

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
