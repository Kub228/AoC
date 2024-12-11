filename = 'AoC\\2024\\files_txt\\9.txt'

with open(filename, 'r') as file:
    for line in file:
        numbers = [int(num) for num in line]


def sol1(numbers):

    free_or_not = 0
    id_assigned = -1
    ID_disk_not_sorted = []
    ID_disk_sorted = []
    total = 0

    for i in range(len(numbers)):
        free_or_not += 1

        if free_or_not % 2 == 0:
            for j in range(numbers[i]):
                ID_disk_not_sorted.append('.')

        else:
            id_assigned += 1
            for j in range(numbers[i]):
                ID_disk_not_sorted.append(id_assigned)

    
    
    for i in range(len(ID_disk_not_sorted)):
        if ID_disk_not_sorted[i] not in [0,1,2,3,4,5,6,7,8,9]:
            
            ID_disk_not_sorted[i], ID_disk_not_sorted[-1] = ID_disk_not_sorted[-1], ID_disk_not_sorted[i]
                
    print(f'Not sorted: {ID_disk_not_sorted}')

    for i in range(len(ID_disk_sorted)):
        equals = i*ID_disk_sorted[i]
        total += equals
        equals = 0

    print(f'Sorted: {ID_disk_sorted}')

    print(f'Sum: {total}')


sol1(numbers)