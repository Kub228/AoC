filename = 'AoC\\2024\\files_txt\\12.txt'

with open(filename, 'r') as file:
    grid = [list(line.strip()) for line in file]

def sol1(grid):
    def dfs(x, y, letter):
        
        if (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != letter or (x, y) in visited):
            return 0, 0
        
        visited.add((x, y))
        
        area = 1
        perimeter = 0
        
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = x + dx, y + dy
            
            if (next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]) or grid[next_x][next_y] != letter):
                perimeter += 1
                
            else:
                next_area, next_perimeter = dfs(next_x, next_y, letter)
                area += next_area
                perimeter += next_perimeter
        
        return area, perimeter

    total = 0
    visited = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in visited and grid[i][j] != ' ':
                area, perimeter = dfs(i, j, grid[i][j])
                total += area * perimeter

    print(f'\nTotal1: {total}')
    
def sol2(grid):
    h, w = len(grid), len(grid[0])
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    seen = set()
    
    def loc(y, x):
        if y < 0 or x < 0:
            return None
        try:
            return grid[y][x]
        except Exception:
            return None
    
    def bfs(y, x):
        grp = set([(y, x)])
        val = grid[y][x]
        cur = [(y, x)]
        while cur:
            nxt = []
            for (y, x) in cur:
                for (dy, dx) in moves:
                    ny, nx = y+dy, x+dx
                    if loc(ny, nx) == val and (ny, nx) not in seen:
                        seen.add((ny, nx))
                        grp.add((ny, nx))
                        nxt.append((ny, nx))
                cur = nxt
        return grp
    
    def sides(grp):
        sseen = set()
        ccs = 0
        for (y, x) in grp:
            for (dy, dx) in moves:
                if (y+dy, x+dx) in grp:
                    continue
                cy, cx = y, x
                while (cy+dx, cx+dy) in grp and (cy+dy, cx+dx) not in grp:
                    cy += dx
                    cx += dy
                if (cy, cx, dy, dx) not in sseen:
                    sseen.add((cy, cx, dy, dx))
                    ccs += 1
        return ccs
    
    total = 0
    for y in range(h):
        for x in range(w):
            if (y, x) in seen:
                continue
            grp = bfs(y, x)
            total += len(grp) * sides(grp)

    print(f'\nTotal2: {total}')

sol1(grid)
sol2(grid)

