# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

class Node:
    def __init__(self, val: str, valid_word=False, children=None):
        self.val = val
        self.valid_word = valid_word
        self.children = {} if children is None else children

class Trie:
    def __init__(self):
        self.head = Node("")

    def insert(self, word: str) -> None:
        node = self.head
        for letter in word:
            if letter not in node.children.keys():
                node.children[letter] = Node(letter)
            node = node.children[letter]
        node.valid_word = True
        
    def search(self, word: str) -> bool:
        node = self.head
        for letter in word:
            if letter not in node.children.keys():
                return False
            node = node.children[letter]
        return node.valid_word

    def startsWith(self, prefix: str) -> bool:
        node = self.head
        for letter in prefix:
            if letter not in node.children.keys():
                return False
            node = node.children[letter]

        return True
        
