# This file has all the problems in the Graphs
# section of the NeetCode150 with the explanations.

from collections import deque

def maxAreaOfIsland(grid):
    stack = []
    area = 0
    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                stack.append((i, j))
                grid[i][j] = 0
                currArea = 0

                while stack:
                    currOne = stack.pop()
                    neighbors = getneighbors(currOne, grid)
                    currArea += 1

                    for x, y in neighbors:
                        grid[x][y] = 0
                        stack.append((x, y))

                area = max(area, currArea)

    return area

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

def orangesRotting(grid):
    m = len(grid)
    n = len(grid[0])
    rotten = deque()
    freshCount = 0
    time = 0

    # Count initial rotten and fresh oranges
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                rotten.append((i, j))      # Add rotten orange to queue
            elif grid[i][j] == 1:
                freshCount += 1            # Count fresh oranges

    if freshCount == 0:
        return 0                          # No fresh oranges, no time needed

    # BFS from initially rotten oranges
    while rotten and freshCount > 0:
        length = len(rotten)

        for i in range(length):
            current = rotten.popleft()
            neighbors = getNeighborsOrange(grid, current)
            for x, y in neighbors:
                freshCount -= 1            # One fresh orange becomes rotten
                rotten.append((x, y))      # Add it to queue for next round

        time += 1                          # One minute passed

    # Time Complexity: O(m * n) -> Each cell is processed at most once.
    # Space Complexity: O(m * n) -> In worst case, all cells added to the queue.

    return time if freshCount == 0 else -1 # If fresh oranges remain, impossible


def getNeighborsOrange(grid, current):
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)] # left, up, right, down
    neighbors = []

    for x, y in directions:
        dx = current[0] + x
        dy = current[1] + y

        # Check bounds and find fresh neighbors
        if (0 <= dx < len(grid)) and (0 <= dy < len(grid[0])):
            if grid[dx][dy] == 1:
                grid[dx][dy] = 2           # Mark as rotten
                neighbors.append((dx, dy))

    return neighbors

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