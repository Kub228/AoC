inpt = '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124'''

with open("AoC\\2025\\txt_files\\d2.txt") as f:
  inpt = f.read()

inpt = inpt.replace("\n", "")
inpt = inpt.strip()
inpt = inpt.split(",")

invalid_ids = []

for i in range(len(inpt)):
    inpt[i] = inpt[i].split("-")

for i in range(len(inpt)):
    for j in range(int(inpt[i][0]),int(inpt[i][1])+1):
        # mid=len(str(j))//2
        # if str(j)[:mid] == str(j)[mid:]:
        #     print(f'{i} is invalid')
        #     invalid_ids.append(j)
        
        temp = ''
        k = 0
        while k < len(str(j)):
            if str(j)[k] not in temp:
                temp += str(j)[k]
                k += 1
            else:
                l = k
                h = len(temp)  
                while l + h <= len(str(j)) and str(j)[l:l+h] == temp:
                    l += h
                    
                if l == len(str(j)):
                    invalid_ids.append(j)
                    break
                        
                else:
                    temp += str(j)[k]
                    k += 1

print(invalid_ids)
print(sum(invalid_ids))

    