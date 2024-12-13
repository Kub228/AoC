import math

def calc_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def find_antinode_points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    dx = x2 - x1
    dy = y2 - y1
    
    dist = calc_distance(p1, p2)
    if dist == 0:
        return []
    
    ux = dx / dist
    uy = dy / dist
    
    antinodes = []
    
    ax1 = x1 - dist * ux
    ay1 = y1 - dist * uy
    antinodes.append((ax1, ay1))
    
    ax2 = x2 + dist * ux
    ay2 = y2 + dist * uy
    antinodes.append((ax2, ay2))
    
    return antinodes

def sol1(grid):
    height = len(grid)
    width = len(grid[0])
    
    frequencies = {}
    for y in range(height):
        for x in range(width):
            if grid[y][x] != '.':
                freq = grid[y][x]
                if freq not in frequencies:
                    frequencies[freq] = []
                frequencies[freq].append((x, y))
    
    antinodes = set()
    
    for freq, positions in frequencies.items():
        if len(positions) < 2:
            continue
        
        for i, pos1 in enumerate(positions):
            for j, pos2 in enumerate(positions[i+1:], i+1):
                new_antinodes = find_antinode_points(pos1, pos2)
                
                for ax, ay in new_antinodes:
                    if 0 <= ax < width and 0 <= ay < height:
                        antinodes.add((round(ax), round(ay)))
    
    return len(antinodes)


def parse_input(grid):
    antennas = {}
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
    return antennas

def find_collinear_points(antennas, width, height):
    def is_collinear(p1, p2, p3):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        return (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)

    antinodes = set()
    for freq, positions in antennas.items():
        if len(positions) < 2:
            continue
            
        antinodes.update(positions)
        
        for i, pos1 in enumerate(positions):
            for j, pos2 in enumerate(positions[i+1:], i+1):
                x1, y1 = pos1
                x2, y2 = pos2
                
                if x2 < x1:
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
                
                dx = x2 - x1
                dy = y2 - y1
                
                gcd = math.gcd(abs(dx) if dx != 0 else 1, abs(dy) if dy != 0 else 1)
                dx_step = dx // gcd
                dy_step = dy // gcd
                
                x, y = x1, y1
                while 0 <= x < width and 0 <= y < height:
                    antinodes.add((x, y))
                    x += dx_step
                    y += dy_step
                
                x, y = x1 - dx_step, y1 - dy_step
                while 0 <= x < width and 0 <= y < height:
                    antinodes.add((x, y))
                    x -= dx_step
                    y -= dy_step
    return antinodes

def sol2(grid):
    height = len(grid)
    width = len(grid[0])
    antennas = parse_input(grid)
    antinodes = find_collinear_points(antennas, width, height)
    return len(antinodes)





def main():
    with open('AoC\\2024\\files_txt\\8.txt', 'r') as file:
        grid = [list(line.strip()) for line in file]
        
    # Run both solutions
    result1 = sol1(grid)  # Your existing solution for part 1
    result2 = sol2(grid)
    
    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()
