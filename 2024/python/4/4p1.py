with open("2024_f\\4.txt", "r") as file:
    grid = [line.strip() for line in file.readlines()]

def check_word(grid, i, j, di, dj, word):
    if (0 <= i + di * (len(word)-1) < len(grid) and 
        0 <= j + dj * (len(word)-1) < len(grid[0])):
        
        for k in range(len(word)):
            if grid[i + di*k][j + dj*k] != word[k]:
                return False
        return True
    return False
    
def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0]) 
    count = 0
    
    
    directions = [
        (0,1),   # right
        (1,0),   # down
        (1,1),   # diagonal down-right
        (-1,1),  # diagonal up-right
        (0,-1),  # left
        (-1,0),  # up
        (-1,-1), # diagonal up-left
        (1,-1)   # diagonal down-left
    ]
    
    for i in range(rows):
        for j in range(cols):
            for di, dj in directions:
                if check_word(grid, i, j, di, dj, "XMAS"):
                    count += 1
    
    return count

result = find_xmas(grid)
print(result)
