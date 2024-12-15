from collections import deque
import math

filename = 'AoC\\2024\\files_txt\\11.txt'

with open(filename, 'r') as file:
    for line in file:
        stones = [int(num) for num in line.split()]
        


def sol1(stones):
    
    
    iterations = 25
    result = []
    for iteration in range(iterations):
        for stone in stones:
            if stone == 0:
                result.append(1)
                continue
                
            
            num_str = str(stone)
            
            if len(num_str) % 2 == 0:
                
                mid = len(num_str) // 2
                first_half = int(num_str[:mid])
                second_half = int(num_str[mid:])
                
                if second_half == 0:
                    result.append(first_half)
                    result.append(0)
                else:
                    result.append(first_half)
                    result.append(second_half)
            else:
                
                result.append(stone * 2024)
                
        stones = result
        result = []
        print(f'Current iteration: {iteration}/{iterations}')
        
    
    total = len(stones)
                
    print(f'Solution1: {total}')
    
#optimised algorythm v2
    
def sol2(stones):
    iterations = 75
    memo = {}
    
    def process_number(n):
        if n in memo:
            return memo[n]
        
        if n == 0:
            result = [1]
        elif n % 2 == 0:
            digits = int(math.log10(n)) + 1
            if digits % 2 == 0:
                divisor = 10 ** (digits // 2)
                first_half = n // divisor
                second_half = n % divisor
                result = [first_half, second_half] if second_half != 0 else [first_half, 0]
            else:
                result = [n * 2024]
        else:
            result = [n * 2024]
        
        memo[n] = result
        return result

    stones = deque(stones)
    for iteration in range(iterations):
        new_stones = deque()
        while stones:
            stone = stones.popleft()
            new_stones.extend(process_number(stone))
        stones = new_stones
        print(f'Current iteration: {iteration}/{iterations}')
    
    total = len(stones)
    print(f'Solution: {total}')
    
    
#optimised algorythm v3

def sol2_v2(stones):
    memo = {}
    iterations = 75

    def count(remaining, num):
        if (remaining, num) in memo:
            return memo[(remaining, num)]
        
        if remaining == 0:
            return 1
        
        if num == 0:
            result = count(remaining - 1, 1)
        else:
            digit_count = math.floor(math.log10(num)) + 1
            if digit_count % 2 == 0:
                div_factor = 10 ** (digit_count // 2)
                left, right = num // div_factor, num % div_factor
                result = count(remaining - 1, left) + count(remaining - 1, right)
            else:
                result = count(remaining - 1, 2024 * num)
        
        memo[(remaining, num)] = result
        return result

    total = sum(count(iterations, stone) for stone in stones)
    print(f'Solution2: {total}')

    
sol1(stones)
sol2_v2(stones)
