class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = [[False] * col for _ in range(row)]
        q = deque()

        land, borderland = 0, 0
        for r in range(row):
            for c in range(col):
                land += grid[r][c]
                if (grid[r][c] == 1 and (r in [0, row - 1] or c in [0, col - 1])):
                    q.append((r,c))
                    visit[r][c] = True
        
        while q:
            r, c = q.popleft()
            borderland += 1
            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                if (0 <= nr < row and 0 <= nc < col and
                    grid[nr][nc] == 1 and not visit[nr][nc]):
                    q.append((nr,nc))
                    visit[nr][nc] = True
        
        return land - borderland