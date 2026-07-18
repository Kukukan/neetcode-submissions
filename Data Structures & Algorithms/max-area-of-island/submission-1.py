class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        vis = set()
        def dfs(r, c):
            tmp = 1
            if (r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or (r,c) in vis):
                return 0
            vis.add((r,c))
            tmp += dfs(r+1, c)
            tmp += dfs(r-1, c)
            tmp += dfs(r, c+1)
            tmp += dfs(r, c-1)
            return tmp
        ans = 0
        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dfs(r,c))
        return ans