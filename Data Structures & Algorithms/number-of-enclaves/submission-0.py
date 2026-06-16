class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(r, c):
            if (r < 0 or c < 0 or
                r == row or c == col or
                not grid[r][c] or (r, c) in visit):
                return 0
            visit.add((r, c))
            res = 1
            for dr, dc in dir:
                res += dfs(r + dr, c + dc)
            return res

        visit = set()
        land, borderland = 0, 0
        for r in range(row):
            for c in range(col):
                land += grid[r][c]
                if (grid[r][c] and (r, c) not in visit and
                    (c in [0, col - 1] or r in [0, row - 1])):
                    borderland += dfs(r, c)

        return land - borderland