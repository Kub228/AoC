filename = 'AoC\\2024\\files_txt\\9.txt'


def sol1(numbers):
    global pace

    numbers = [int(digit) for digit in str(numbers)]
    
    free_or_not = 0
    id_assigned = -1
    ID_disk_sorted = []
    total = 0
    
    pace = 100
    
    for i in range(len(numbers)):
        free_or_not += 1

        if free_or_not % 2 == 0:
            for j in range(numbers[i]):
                ID_disk_sorted.append('.')
        else:
            id_assigned += 1
            for j in range(numbers[i]):
                ID_disk_sorted.append(id_assigned)

    print(f'Not updated: {ID_disk_sorted}')
    
    new_last = len(ID_disk_sorted)-1
    
    for i in range(len(ID_disk_sorted)):
        
        
        if i >= new_last:
            break
        
        while ID_disk_sorted[new_last] == '.' and ID_disk_sorted[i] == '.':
            new_last -= 1
            
        if ID_disk_sorted[i] == '.':
            ID_disk_sorted[i], ID_disk_sorted[new_last] = ID_disk_sorted[new_last], ID_disk_sorted[i]
            
        
        if i % 1000 == 0:
            print(f'\nUpdating{i}:    {ID_disk_sorted}')
                
    print(f'Updated:     {ID_disk_sorted}')
    
    
    
    new_list = []
    for x in ID_disk_sorted:
        if x != '.':
            new_list.append(x)
    ID_disk_sorted = new_list

    for i in range(len(ID_disk_sorted)):
        equals = i*ID_disk_sorted[i]
        total += equals
        equals = 0

    print(f'Sum: {total}')
    total = str(total)
    print(f'Digits: {len(total)}')
    
def sol2(numbers):
    numbers = [int(digit) for digit in str(numbers)]
    ID_disk_sorted = []
    id_assigned = -1
    
    for i in range(len(numbers)):
        if i % 2 == 0:
            id_assigned += 1
            ID_disk_sorted.extend([id_assigned] * numbers[i])
        else:
            ID_disk_sorted.extend(['.'] * numbers[i])

    print(f'Not updated: {ID_disk_sorted}')

    max_id = id_assigned
    for current_id in range(max_id, -1, -1):
        file_blocks = [(i, block) for i, block in enumerate(ID_disk_sorted) if block == current_id]
        if not file_blocks:
            continue
        
        file_length = len(file_blocks)
        
        free_space_start = None
        free_space_count = 0
        
        for i, block in enumerate(ID_disk_sorted):
            if block == '.':
                if free_space_start is None:
                    free_space_start = i
                free_space_count += 1
                
                if free_space_count == file_length:
                    if free_space_start < file_blocks[0][0]:
                        for j in range(file_length):
                            ID_disk_sorted[free_space_start + j] = current_id
                            ID_disk_sorted[file_blocks[j][0]] = '.'
                    break
            else:
                free_space_start = None
                free_space_count = 0
        
        
        if i % pace == 0:
            print(f'\nUpdating: {i//pace}')

    print(f'Updated: {ID_disk_sorted}')

    total = 0
    for i, block in enumerate(ID_disk_sorted):
        if block != '.':
            total += i * block
    
    print(f'Total: {total}')


with open(filename, 'r') as file:
    content = file.read().strip()
    sol2(content)

