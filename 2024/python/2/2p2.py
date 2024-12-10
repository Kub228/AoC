def is_safe(sequence):
    # Check if sequence is already safe without removing any number
    incrs = all(sequence[i] < sequence[i+1] for i in range(len(sequence)-1))
    dcrs = all(sequence[i] > sequence[i+1] for i in range(len(sequence)-1))
    valid_diff = all(1 <= abs(sequence[i] - sequence[i+1]) <= 3 for i in range(len(sequence)-1))
    
    if (incrs or dcrs) and valid_diff:
        return True
    
    # Try removing each number and check if resulting sequence is safe
    for i in range(len(sequence)):
        new_seq = sequence[:i] + sequence[i+1:]
        
        incrs = all(new_seq[j] < new_seq[j+1] for j in range(len(new_seq)-1))
        dcrs = all(new_seq[j] > new_seq[j+1] for j in range(len(new_seq)-1))
        valid_diff = all(1 <= abs(new_seq[j] - new_seq[j+1]) <= 3 for j in range(len(new_seq)-1))
        
        if (incrs or dcrs) and valid_diff:
            return True
            
    return False

f = open("2024_f\\2.txt", "r")
f_r = f.read()

safe = 0
eval = []
n = []

for i in f_r:
    if ' ' != i and '\n' != i:
        n.append(i)
    
    if ' ' == i or '\n' == i:
        if n:
            n = ''.join(n)
            n = int(n)
            eval.append(n)
            n = []
            
        if '\n' == i:
            if is_safe(eval):
                safe += 1
            eval = []

print(safe)
