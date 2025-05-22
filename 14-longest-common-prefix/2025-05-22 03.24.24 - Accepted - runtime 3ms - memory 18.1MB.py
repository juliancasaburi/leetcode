class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def longest_common_prefix(self):
        prefix = ""
        node = self.root

        while True:
            if len(node.children) != 1 or node.is_end:
                break

            ch, next_node = next(iter(node.children.items()))
            prefix += ch
            node = next_node

        return prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        trie = Trie()
        for word in strs:
            trie.insert(word)

        return trie.longest_common_prefix()
