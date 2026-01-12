def foreignDictionary(self, words: List[str]) -> str:
    alphabets = {}
    n = len(words)

    for word in words:
        for w in word:
            if w not in alphabets:
                alphabets[w] = set()

    for i in range(n - 1):
        w1 = words[i]
        w2 = words[i + 1]

        minLen = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
            return ""
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                alphabets[c1].add(c2)
                break

    # Need to run BFS from each char
    res = []
    vis = {}
    for char in alphabets.keys():
        if self.BFS(alphabets, char, res, vis):
            return ""

    res.reverse()
    return "".join(res)


def BFS(self, graph, char, res, vis):
    if char in vis:
        return vis[char]

    vis[char] = True  # True means we are visiting this node

    for adj in graph[char]:
        # Need to run BFS on this now
        if self.BFS(graph, adj, res, vis):
            return True

    vis[char] = False
    res.append(char)
