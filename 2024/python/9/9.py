filename = 'AoC\\2024\\files_txt\\9.txt'


def sol1(numbers):

    numbers = [int(digit) for digit in str(numbers)]
    
    free_or_not = 0
    id_assigned = -1
    ID_disk_sorted = []
    total = 0

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
    free_or_not = 0
    id_assigned = -1
    ID_disk_sorted = []
    total = 0
    
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
    
    for i in range(id_assigned, -1, -1):
        file_count = 0
        for j in range(len(ID_disk_sorted)):
            if ID_disk_sorted[j] == i:
                file_count += 1
                
        if file_count == 0:
            continue
            
        for j in range(len(ID_disk_sorted)):
            free_count = 0
            for k in range(j, min(j + file_count, len(ID_disk_sorted))):
                if ID_disk_sorted[k] == '.':
                    free_count += 1
                    
            if free_count == file_count:
                file_pos = -1
                for k in range(len(ID_disk_sorted)):
                    if ID_disk_sorted[k] == i:
                        file_pos = k
                        break
                        
                if file_pos > j:
                    for k in range(file_count):
                        ID_disk_sorted[j + k] = i
                        ID_disk_sorted[file_pos + k] = '.'
                break
            
            if i % 1000 == 0:
                print(f'\nUpdating{i}:    {ID_disk_sorted}')
    
    print(f'Updated: {ID_disk_sorted}')
    
    for i in range(len(ID_disk_sorted)):
        if ID_disk_sorted[i] != '.':
            total += i * ID_disk_sorted[i]
            
    print(total)


    


with open(filename, 'r') as file:
    content = file.read().strip() 
    numbers = content  
    # sol1(numbers)
    sol2(numbers)