import re

def sol1(memory):
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, memory)
    total = sum(int(x) * int(y) for x, y in matches)
    return total

def sol2(memory):
    mul_pattern = r'mul\((\d+),(\d+)\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    
    total = 0
    enabled = True
    
    tokens = re.split(r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))', memory)
    
    for token in tokens:
        if re.match(mul_pattern, token):
            if enabled:
                x, y = map(int, re.findall(r'\d+', token))
                total += x * y
        elif re.match(do_pattern, token):
            enabled = True
        elif re.match(dont_pattern, token):
            enabled = False
    
    return total

with open("AoC\\2024\\files_txt\\3.txt", 'r') as file:
    memory = file.read().strip()

print(f"Part 1 result: {sol1(memory)}")
print(f"Part 2 result: {sol2(memory)}")
