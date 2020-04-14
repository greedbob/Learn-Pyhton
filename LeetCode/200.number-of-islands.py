class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid:
            num = 0
            # island = []
            for i, line in enumerate(grid):
                for j, dot in enumerate(line):
                    if dot=='1':
                        num += 1
                        self.infect(grid, [i, j])
            return num
        else:
            return 0
    
    def trace(self, grid, dot):
        done = []
        q = [dot]
        height, lenght = len(grid), len(grid[0])
        while q:
            [x, y] = q.pop(0)
            done.append([x, y])
            if x > 0 and grid[x-1][y] == '1' and [x-1, y] not in done + q:
                q.append([x-1, y])
            if x < height-1 and grid[x+1][y] == '1' and [x+1, y] not in done + q:
                q.append([x+1, y])
            if y > 0 and grid[x][y-1] == '1' and [x, y-1] not in done + q:
                q.append([x, y-1])
            if y < lenght-1 and grid[x][y+1] == '1' and [x, y+1] not in done + q:
                q.append([x, y+1])
        return done
    
    def infect(self, grid, dot):
        [x, y] = dot
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != '1':
            pass
        else:
            grid[x][y] = '2'
            self.infect(grid, [x+1, y])
            self.infect(grid, [x-1, y])
            self.infect(grid, [x, y+1])
            self.infect(grid, [x, y-1])
