
class Solution:
    def getTotalIsles(self, grid):
        if not grid:
            return 0
        
        self.rows = len(grid)
        self.cols = len(grid[0])
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        island_count = 0

        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == 'L' and not visited[r][c]:
                    self.dfs(grid, r, c, visited)
                    island_count += 1
        
        return island_count

    def dfs(self, grid, r, c, visited):
        if r < 0 or r >= self.rows or c < 0 or c >= self.cols or visited[r][c] or grid[r][c] == 'W':
            return
        # Mark this cell as visited
        visited[r][c] = True
        
        # Explore the four possible directions (up, down, left, right)
        self.dfs(grid, r - 1, c, visited)  # up
        self.dfs(grid, r + 1, c, visited)  # down
        self.dfs(grid, r, c - 1, visited)  # left
        self.dfs(grid, r, c + 1, visited)  # right
