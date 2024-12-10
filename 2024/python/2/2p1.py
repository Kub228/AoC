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
            incrs = all(eval[i] < eval[i+1] for i in range(len(eval)-1))
            dcrs = all(eval[i] > eval[i+1] for i in range(len(eval)-1))
            
            valid_diff = all(1 <= abs(eval[i] - eval[i+1]) <= 3 for i in range(len(eval)-1))
            
            if (incrs or dcrs) and valid_diff:
                safe += 1
                
            eval = []

print(safe)
