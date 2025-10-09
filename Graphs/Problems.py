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