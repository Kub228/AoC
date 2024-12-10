with open("2024_f\\4.txt", "r") as file:
    # Clean up the input grid by stripping whitespace
    grid = [line.strip() for line in file.readlines()]

def check_word(grid, i, j, di, dj, word):
    # Check if word fits within grid bounds in this direction
    if (0 <= i + di * (len(word)-1) < len(grid) and 
        0 <= j + dj * (len(word)-1) < len(grid[0])):
        
        # Check each character of the word
        for k in range(len(word)):
            if grid[i + di*k][j + dj*k] != word[k]:
                return False
        return True
    return False
    
def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])  # len of first row for columns
    count = 0
    
    # Define all 8 directions to search
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
