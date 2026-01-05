class PrefixTree:
    class TrieNode():
        def __init__(self):
            self.children = {}
            self.isEnd = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        n = len(word)

        for i in range(n):
            char = word[i]

            if char not in cur.children:
                cur.children[char] = self.TrieNode()

            cur = cur.children[char]

        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        n = len(word)

        for i in range(n):
            char = word[i]

            if not cur.children[char]:
                return False

            cur = cur.children[char]

        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children[c]:
                return False

            cur = cur.children[c]

        return True


class WordDictionary:
    class TrieNode():
        def __init__(self):
            self.children = {}
            self.isEnd = False

    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = self.TrieNode()

            cur = cur.children[c]

        cur.isEnd = True

    def search(self, word: str) -> bool:
        def DFS(j, root):
            cur = root
            n = len(word)

            for i in range(j, n):
                char = word[i]

                if char == '.':
                    children = cur.children.values()

                    for c in children:
                        check = DFS(i + 1, c)

                        if check:
                            return True

                if char not in cur.children:
                    return False

                cur = cur.children[char]

            return cur.isEnd

        return DFS(0, self.root)

