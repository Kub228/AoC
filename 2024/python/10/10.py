filename = 'AoC\\2024\\files_txt\\10.txt'

def sol1(grid):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
    scores = []

    def dfs(x, y, current_height, visited, reached_nines):
        if current_height == 9:
            if (x, y) not in reached_nines:
                reached_nines.add((x, y))
                return 1
            return 0
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(grid) and 
                0 <= ny < len(grid[0]) and 
                (nx, ny) not in visited and
                grid[nx][ny] != '.' and 
                int(grid[nx][ny]) == current_height + 1):
                count += dfs(nx, ny, current_height + 1, visited | {(nx, ny)}, reached_nines)
        return count

    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value == '0':
                reached_nines = set()
                score = dfs(x, y, 0, {(x, y)}, reached_nines)
                scores.append(score)
                print(f"Trailhead at [{x},{y}] has score: {score}")

    return scores

def sol2(grid):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
    ratings = []

    def dfs(x, y, current_height, visited):
        if current_height == 9:
            return 1
            
        total_paths = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(grid) and 
                0 <= ny < len(grid[0]) and 
                (nx, ny) not in visited and
                grid[nx][ny] != '.' and 
                int(grid[nx][ny]) == current_height + 1):
                total_paths += dfs(nx, ny, current_height + 1, visited | {(nx, ny)})
        return total_paths

    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value == '0':
                rating = dfs(x, y, 0, {(x, y)})
                ratings.append(rating)
                print(f"Trailhead at [{x},{y}] has rating: {rating}")

    return ratings


with open(filename, 'r') as file:
    grid = [list(line.strip()) for line in file]
    
total = sol1(grid)
total = sum(total)
print(f"Sol1 total: {total}")

total = sol2(grid)
total = sum(total)
print(f"Sol2 total: {total}")
