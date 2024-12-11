filename = 'files_txt\\7.txt'

converted_input = []
with open(filename, 'r') as file:
    for line in file:
        numbers = [int(num) for num in line.split()]
        converted_input.append(numbers)

#part1

def evaluate_left_to_right1(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        else: 
            result *= numbers[i + 1]
    return result

def check_combinations1(target, numbers):
    if len(numbers) == 2:  
        if target == numbers[0] * numbers[1]:
            return True
        if target == numbers[0] + numbers[1]:
            return True
        return False
    
    
    num_operators = len(numbers) - 1
    for i in range(2 ** num_operators):  
        operators = []
        for j in range(num_operators):
            if (i >> j) & 1:
                operators.append('+')
            else:
                operators.append('*')
        
        if evaluate_left_to_right1(numbers, operators) == target:
            return True
    
    return False

def sol1(converted_input):
    total = 0
    for index, row in enumerate(converted_input, 1):
        target = row[0]
        numbers = row[1:]
        
        if check_combinations1(target, numbers):
            total += target
            
        if index % 50 == 0:
            print(f"Part 1 - Processed {index} rows... Current total: {total}")
            
    return total

#part2

def evaluate_left_to_right2(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        else:
            result = int(str(result) + str(numbers[i + 1]))
    return result

def check_combinations2(target, numbers):
    if len(numbers) == 2:  
        if target == numbers[0] * numbers[1]:
            return True
        if target == numbers[0] + numbers[1]:
            return True
        if target == int(str(numbers[0]) + str(numbers[1])):
            return True
        return False
    
    num_operators = len(numbers) - 1
    for i in range(3 ** num_operators): 
        operators = []
        temp = i
        for j in range(num_operators):
            remainder = temp % 3
            if remainder == 0:
                operators.append('+')
            elif remainder == 1:
                operators.append('*')
            else:
                operators.append('||')
            temp //= 3
        
        if evaluate_left_to_right2(numbers, operators) == target:
            return True
    
    return False


def sol2(converted_input):
    total = 0
    for index, row in enumerate(converted_input, 1):
        target = row[0]
        numbers = row[1:]
        
        if check_combinations2(target, numbers):
            total += target
            
        if index % 25 == 0:
            print(f"Part 2 - Processed {index} rows... Current total: {total}")
    
    return total


print('\nanswer1:', sol1(converted_input))
print('\nanswer2:', sol2(converted_input))

