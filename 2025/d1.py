inpt = '''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''.split()

with open("AoC\\2025\\txt_files\\d1.txt") as f:
  inpt = f.read().split()

# i=0
# dial=50
# pwd = 0

# while i < len(inpt):
#     print('Global_Dial:',dial)
#     if inpt[i][0] == 'L':
#         inpt[i]=list(inpt[i])
#         inpt[i].pop(0)
#         inpt[i]=int(''.join(inpt[i]))
#         print('Rotation_L:',inpt[i],'After_Rotation:',dial-inpt[i])
        
#         pwd+=(inpt[i]-dial)//100
        
#         dial = (dial-int(inpt[i]))%100
        
#     elif inpt[i][0] == 'R':
#         inpt[i]=list(inpt[i])
#         inpt[i].pop(0)
#         inpt[i]=int(''.join(inpt[i]))
#         print('Rotation_R:',inpt[i],'After_Rotation:',dial+inpt[i])
        
#         pwd+=(inpt[i]+dial)//100+1
        
#         dial = (dial+int(inpt[i]))%100
    
#     if dial==0:
#         pwd+=1
        
#     print(pwd)
    
#     i += 1


def zero_crosses(start, direction, dist):
    if dist == 0:
        return 0

    if direction == 'L':
        k_first = start % 100
    else:
        k_first = (100 - start) % 100

    if k_first == 0:
        k_first = 100

    if dist < k_first:
        return 0

    return 1 + (dist - k_first) // 100


dial = 50
pwd = 0

for instr in inpt:
    direction = instr[0]
    dist = int(instr[1:])      

    pwd += zero_crosses(dial, direction, dist)

    if direction == 'L':
        dial = (dial - dist) % 100
    else:
        dial = (dial + dist) % 100

print(pwd)