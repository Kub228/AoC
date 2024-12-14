with open("2024_f\\4.txt", "r") as file:
    
    grid = [line.strip() for line in file.readlines()]

def check_xmas_pattern(grid, i, j):
    if i + 2 >= len(grid) or j - 1 < 0 or j + 1 >= len(grid[0]):
        return False
        
    if grid[i+1][j] != 'A':
        return False
        
    
    # Pattern 1:    Pattern 2:    Pattern 3:    Pattern 4:
    # M.S          S.M          S.S          M.M
    # .A.          .A.          .A.          .A.
    # M.S          S.M          M.M          S.S
    
    top_left = grid[i][j-1]
    top_right = grid[i][j+1]
    bottom_left = grid[i+2][j-1]
    bottom_right = grid[i+2][j+1]
    
    pattern1 = ((top_left == 'M' and top_right == 'S' and
                bottom_left == 'M' and bottom_right == 'S') or
               (top_left == 'S' and top_right == 'M' and
                bottom_left == 'S' and bottom_right == 'M'))
                
    pattern2 = (top_left == 'S' and top_right == 'S' and
               bottom_left == 'M' and bottom_right == 'M')
               
    pattern3 = (top_left == 'M' and top_right == 'M' and
               bottom_left == 'S' and bottom_right == 'S')
    
    return pattern1 or pattern2 or pattern3


def count_xmas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    for i in range(rows-2):
        for j in range(1, cols-1):
            if check_xmas_pattern(grid, i, j):
                count += 1
    
    return count


result = count_xmas_patterns(grid)
print(result)
