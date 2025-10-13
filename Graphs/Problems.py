# This file has all the problems in the Graphs
# section of the NeetCode150 with the explanations.

from collections import deque

def numIslands(self, grid):
    islands = 0
    queue = deque()

    for i in range(len(grid)):
        for j in range(len(grid[0])):

            if grid[i][j] == "1":
                queue.append((i, j))
                grid[i][j] = "0"
                islands += 1

                while queue:
                    current = queue.popleft()

                    for neighbor in self.getneighbors(grid, current):
                        grid[neighbor[0]][neighbor[1]] = "0"
                        queue.append(neighbor)

    return islands

def orangesRotting(grid)
    m = len(grid)
    n = len(grid[0])
    rotten = deque()
    freshCount = 0
    time = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                rotten.append((i, j))
            elif grid[i][j] == 1:
                freshCount += 1

    if freshCount == 0:
        return 0

    while rotten and freshCount > 0:
        length = len(rotten)

        for i in range(length):
            current = rotten.popleft()
            neighbors = self.getNeighborsOrange(grid, current)
            for x, y in neighbors:
                freshCount -= 1
                rotten.append((x, y))

        time += 1

    return time if freshCount == 0 else -1

def getneighbors(self, grid, curr):
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for x, y in directions:
        dx = curr[0] + x
        dy = curr[1] + y

        if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]):
            if grid[dx][dy] == "1":
                neighbors.append((dx, dy))

    return neighbors