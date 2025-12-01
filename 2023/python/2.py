import re

filename = 'AoC\\2023\\files_txt\\2.txt'

with open(filename) as file:
    games = [line.strip() for line in file]

def sol1(games):
    r = 12
    g = 13
    b = 14 
    
    pattern = r'(\d+)\s+(red|green|blue)'
    total = 0
    
    for game_index, game in enumerate(games):
        game_match = re.findall(pattern, game)
        valid = True
        
        for count, color in game_match:
            count = int(count)
            if (color == 'red' and count > r) or \
               (color == 'green' and count > g) or \
               (color == 'blue' and count > b):
                valid = False
                break
        
        if valid == True:
            total += game_index + 1
            
    print(f'Total1: {total}')
    
def sol2(games):
    pattern = r'(\d+)\s+(red|green|blue)'
    total = 0
    
    for game in games:
        game_match = re.findall(pattern, game)
        min_cubes = {'red': 0, 'green': 0, 'blue': 0}
        
        for count, color in game_match:
            count = int(count)
            min_cubes[color] = max(min_cubes[color], count)
        
        power = min_cubes['red'] * min_cubes['green'] * min_cubes['blue']
        total += power
    
    print(f'Total2: {total}')


sol1(games)
sol2(games)
