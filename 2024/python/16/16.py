filename = 'AoC\\2024\\files_txt\\16.txt'

with open(filename, 'r') as file:
    grid = [list(line.strip()) for line in file]

#To find out where are we initially standing

# for y in range(len(grid)):
#         for x in range(len(grid[y])):
#             if grid[y][x] in 'S':
#                 curretly_standing = (x,y)
                
# print(curretly_standing)

def sol1(grid):
    facing_side = [(0,-1),(-1,0),(0,1),(1,0)]
    currently_facing = (1,0)
    currently_standing = (1, 13)
    visited = set()
    
    print("Start:", currently_facing)
    
    while True:
        direction = tuple(x + y for x, y in zip(currently_facing, currently_standing))
        
        if (not (0 <= direction[1] < len(grid) and 0 <= direction[0] < len(grid[0])) or 
            grid[direction[1]][direction[0]] == "#"):
            print(f"Hit wall at {direction}")
            for facing in facing_side:
                new_direction = tuple(x + y for x, y in zip(facing, currently_standing))
                if (0 <= new_direction[1] < len(grid) and 
                    0 <= new_direction[0] < len(grid[0]) and 
                    grid[new_direction[1]][new_direction[0]] in ".E" and 
                    new_direction not in visited):
                    currently_facing = facing
                    print(f"New direction: {currently_facing}")
                    break
        
        currently_standing = direction
        visited.add(currently_standing)
        
        if grid[currently_standing[1]][currently_standing[0]] == "E":
            print("Reached the end!")
            break
            
        print(f"Current position: {currently_standing}, Facing: {currently_facing}")






                
sol1(grid)