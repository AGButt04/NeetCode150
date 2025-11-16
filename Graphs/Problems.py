# This file has all the problems in the Graphs
# section of the NeetCode150 with the explanations.
import collections
import math
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(self, node):
    if not node:
        return None

    clone = {}
    queue = deque()
    clone[node] = Node(node.val)
    queue.append(node)

    while queue:
        curr_node = queue.popleft()
        curr_neighbors = curr_node.neighbors

        for n in curr_neighbors:
            if n not in clone:
                clone[n] = Node(n.val)
                queue.append(n)

            clone[curr_node].neighbors.append(clone[n])

    return clone[node]

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

def islandsAndTreasure(self, grid) -> None:
    inf = math.pow(2, 31) - 1
    queue = collections.deque()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                queue.append((i, j))

    while queue:
        cx, cy = queue.popleft()
        neighbors = self.get_neighbors(grid, cx, cy, inf)

        for nx, ny in neighbors:
            grid[nx][ny] = grid[cx][cy] + 1
            queue.append((nx, ny))

def get_neighbors(self, grid, i, j, inf):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    neighbors = []

    for x, y in directions:
        dx = i + x
        dy = j + y

        if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]):
            if grid[dx][dy] == inf:
                neighbors.append((dx, dy))

    return neighbors

def pacificAtlantic(self, heights):
    cells = set()  # use set to remove duplicates
    m = len(heights)
    n = len(heights[0])

    # ---- Atlantic (bottom + right edges) ----
    for col in range(n):
        curr = (0, col)
        if self.BFS(heights, curr, "Atlantic"):
            cells.add((0, col))

    for row in range(m):
        curr = (row, 0)
        if self.BFS(heights, curr, "Atlantic"):
            cells.add((row, 0))

    # ---- Pacific (top + left edges) ----
    for col in range(n):
        curr = (m - 1, col)
        if self.BFS(heights, curr, "Pacific"):
            cells.add((m - 1, col))

    for row in range(m):
        curr = (row, n - 1)
        if self.BFS(heights, curr, "Pacific"):
            cells.add((row, n - 1))

    # ---- Interior cells ----
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            curr = (i, j)
            if self.BFS(heights, curr, "Pacific") and self.BFS(heights, curr, "Atlantic"):
                cells.add((i, j))  # set removes duplicates

    # convert set to list format
    return [[x, y] for (x, y) in cells]

def BFS(self, heights, curr, ocean):
    queue = collections.deque([curr])
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    visited = {curr}
    m, n = len(heights), len(heights[0])

    while queue:
        x, y = queue.popleft()

        # ---- Check Pacific / Atlantic reach ----
        if ocean == 'Atlantic':
            if x == m - 1 or y == n - 1:
                return True
        else:  # Pacific
            if x == 0 or y == 0:
                return True

        # ---- Explore neighbors ----
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if heights[nx][ny] <= heights[x][y]:  # downhill allowed
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))

    return False


