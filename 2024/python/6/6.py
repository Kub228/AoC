filename = 'AoC\\2024\\files_txt\\6.txt'

def read_grid(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file]

def guard_mov(grid, guard_pos, direction):
    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
    row, col = guard_pos
    dx, dy = DIRECTIONS[direction]
    new_row, new_col = row + dx, col + dy
    
    if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
        return (new_row, new_col), direction
    
    if grid[new_row][new_col] != '#':
        return (new_row, new_col), direction
    return (row, col), (direction + 1) % 4

def sol1(grid):
    guard_pos = (79, 87)  # Starting pos
    direction = 0         # Up
    visited = set([guard_pos])
    
    while True:
        new_pos, new_dir = guard_mov(grid, guard_pos, direction)
        row, col = new_pos
        
        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
            break
            
        guard_pos = new_pos
        direction = new_dir
        visited.add(guard_pos)
    
    return len(visited)

def check_loop(grid, test_pos):
    if test_pos == (79, 87):  
        return False
        
    test_grid = [row[:] for row in grid]
    test_grid[test_pos[0]][test_pos[1]] = '#'
    
    guard_pos = (79, 87)
    direction = 0
    visited_states = set()
    steps = 0
    max_steps = len(grid) * len(grid[0]) * 4
    
    while steps < max_steps:
        state = (guard_pos, direction)
        if state in visited_states:
            return True
            
        visited_states.add(state)
        new_pos, new_dir = guard_mov(test_grid, guard_pos, direction)
        
        row, col = new_pos
        if not (0 <= row < len(test_grid) and 0 <= col < len(test_grid[0])):
            return False
            
        guard_pos = new_pos
        direction = new_dir
        steps += 1
    
    return False 

def sol2(grid):
    loop_count = 0
    rows, cols = len(grid), len(grid[0])
    total_positions = rows * cols
    checked = 0
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '.':
                if check_loop(grid, (row, col)):
                    loop_count += 1
                    print(f"Found working position {loop_count} at ({row}, {col})")
            checked += 1
            if checked % 100 == 0:  
                print(f"Checked {checked}/{total_positions} positions...")
    
    return loop_count


def main():
    grid = read_grid(filename)
    print(f"Part 1: {sol1(grid)} steps")
    print(f"Part 2: {sol2(grid)} working positions")

if __name__ == "__main__":
    main()
