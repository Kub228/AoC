from itertools import product
from math import gcd

buttons_a = []
buttons_b = []
prizes = []

with open('AoC\\2024\\files_txt\\13.txt', 'r') as file:
    claw_machine = file.readlines()
    
    for i in range(0, len(claw_machine), 4):
        a_x, a_y = map(int, [x.split('+')[1] for x in claw_machine[i].split(': ')[1].split(', ')])
        buttons_a.append((a_x, a_y))
        
        b_x, b_y = map(int, [x.split('+')[1] for x in claw_machine[i+1].split(': ')[1].split(', ')])
        buttons_b.append((b_x, b_y))
        
        p_x, p_y = map(int, [x.split('=')[1] for x in claw_machine[i+2].split(': ')[1].split(', ')])
        prizes.append((p_x, p_y))


def sol_v1(buttons_a, buttons_b, prizes):
    def calculate_coordinates(button_a, button_b, pushes_a, pushes_b):
        x = pushes_a * button_a[0] + pushes_b * button_b[0]
        y = pushes_a * button_a[1] + pushes_b * button_b[1]
        return (x, y)
    
    solutions = []
    tokens_a = 3
    tokens_b = 1
    
    for i in range(len(prizes)):
        button_a = buttons_a[i]
        button_b = buttons_b[i]
        target = prizes[i]
        
        max_pushes = 200
        found = False
        
        for pushes_a, pushes_b in product(range(max_pushes), repeat=2):
            coords = calculate_coordinates(button_a, button_b, pushes_a, pushes_b)
            if coords == target:
                solutions.append((pushes_a, pushes_b))
                found = True
                break
                
        if not found:
            solutions.append(None)

        if (i+1) % 20 == 0:
            print(f"\nCalculating {i+1}/{len(prizes)}")
            
    total_sol = []
    
    for i, solution in enumerate(solutions):
        if solution:
            total_sol.append(solution[0]*tokens_a)
            total_sol.append(solution[1]*tokens_b)
    
    print(f'Total1: {sum(total_sol)}')
            
sol_v1(buttons_a, buttons_b, prizes)


#v2 

import re

def sol_v2():
    def solve_linear_system(a, b, c, d, e, f):
        
        det = a * d - b * c
        
        if det == 0:
            raise ValueError("No solution")
        
        x = (e * d - b * f) / det
        y = (a * f - e * c) / det
        
        return x, y
    
    machines = []
    grps = open("AoC\\2024\\files_txt\\13.txt").read().strip().split('\n\n')
    for grp in grps:
        lines = grp.split('\n')
        ax, ay = map(int, re.findall(r'(\d+)', lines[0]))
        bx, by = map(int, re.findall(r'(\d+)', lines[1]))
        tx, ty = map(int, re.findall(r'(\d+)', lines[2]))
        machines.append([ax, bx, ay, by, tx, ty])
    
    total_sol = 0
    for machine in machines:
        machine_copy = machine.copy()  
        machine_copy[-1] += 10000000000000
        machine_copy[-2] += 10000000000000
        x, y = solve_linear_system(*machine_copy)
        if int(x) == x and int(y) == y:
            total_sol += x * 3 + y
    
    print(f"Total2: {int(total_sol)}")

sol_v2()
