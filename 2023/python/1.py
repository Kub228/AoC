import re

filename = 'AoC\\2023\\files_txt\\1.txt'

with open(filename) as file:
    f = file.readlines()
f = [line.strip() for line in f]

def sol1(f):
    all_digits = 0
    
    for line in f:
        digits_found = []
        for char in line:
            if char.isdigit():
                digits_found.append(char)
        
        if digits_found:
            n = int(digits_found[0] + digits_found[-1])
            all_digits += n
    
    print(f"Total1: {all_digits}")
    
def sol2(f):
    number_map = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    
    pattern = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))'
    all_digits = 0
    
    for line in f:
        matches = re.finditer(pattern, line)
        digits_found = [match.group(1) for match in matches]
        
        digits = [number_map[d] if d in number_map else d for d in digits_found]
        
        if digits:
            n = int(digits[0] + digits[-1])
            all_digits += n
    
    print(f"Total2: {all_digits}")

sol1(f)
sol2(f)
