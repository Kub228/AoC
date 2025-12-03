inpt = '''987654321111111
811111111111119
234234234234278
818181911112111'''.split()

with open("AoC\\2025\\txt_files\\d3.txt") as f:
  inpt = f.read().split()

# inpt = [list(i) for i in inpt]

inpt = [[int(j) for j in i] for i in inpt]
k = 12

ans = 0
for i in inpt:
    # max_n = 0
    # for j in range(len(i)):
    #     for k in range(len(i)):
    #         if j!=k and k>j:
    #             n = i[j]+i[k]
    #             if int(n)>max_n:
    #                 max_n = int(n)
    # ans += max_n
    remove = len(i) - k
    n = []
    
    for j in i:
        while remove > 0 and n and n[-1] < j:
            n.pop()
            remove -= 1
        n.append(j)
    
    if remove > 0:
        n = n[:-remove]
        
    n = int("".join(str(x) for x in n))
    ans += n
    print(n)
    
print(ans)
                
        