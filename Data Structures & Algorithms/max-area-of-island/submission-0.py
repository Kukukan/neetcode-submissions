class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        vis = set()
        direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        res = 0
        for row in range(rows):
            for col in range(cols):
                tmp = 0
                if grid[row][col] == 1 and (row, col) not in vis:
                    # continue
                    q = deque([(row, col)])
                    vis.add((row, col))
                    while q:
                        r, c = q.popleft()
                        tmp += 1
                        for dr, dc in direc:
                            nr, nc = r + dr, c + dc
                            if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in vis):
                                q.append((nr,nc))
                                vis.add((nr,nc))
                res = max(res, tmp)
        return res