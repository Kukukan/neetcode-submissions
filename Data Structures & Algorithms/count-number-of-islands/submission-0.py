class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        direc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        vis = set()
        def bfs(i, j):
            q = deque([(i,j)])
            vis.add((i,j))
            while q:
                r, c = q.popleft()
                for dr, dc in direc:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1' and (nr, nc) not in vis:
                        vis.add((nr,nc))
                        q.append((nr,nc))
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in vis:
                    res += 1
                    bfs(i, j)
        return res