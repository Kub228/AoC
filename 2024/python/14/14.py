filename = 'AoC\\2024\\files_txt\\14.txt'

with open(filename) as f:
        lines = f.read().strip().split('\n')
        
robots = []
for line in lines:
    pos, vel = line.split()
    px, py = map(int, pos[2:].split(','))
    vx, vy = map(int, vel[2:].split(','))
    robots.append((px, py, vx, vy))

def sol1(robots):
    
    width, height = 101, 103
    
    
    final_positions = []
    for px, py, vx, vy in robots:
        fx = (px + vx * 100) % width
        fy = (py + vy * 100) % height
        final_positions.append((fx, fy))
    
    mid_x = width // 2
    mid_y = height // 2
    quadrants = [0] * 4
    
    for x, y in final_positions:
        if x == mid_x or y == mid_y:
            continue
        
        quadrant = (2 if y > mid_y else 0) + (1 if x > mid_x else 0)
        quadrants[quadrant] += 1
    
    total = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
    
    print(f'Total1: {total}')
    
    
def sol2(robots):
    width, height = 101, 103

    total = 0
    while True:
        visited = set()
        new_robots = []

        for px, py, vx, vy in robots:
            new_px = (px + vx) % width
            new_py = (py + vy) % height

            new_robots.append((new_px, new_py, vx, vy))
            visited.add((new_px, new_py))

        robots = new_robots

        total += 1
        if total % 1000 == 0:
            print(f'Calculating: {total}')
        
        if len(visited) == len(robots):
            break
            
    print(f'Total2: {total}')
    
    
sol1(robots)
sol2(robots)
