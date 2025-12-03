invalid_ids = []
for i in range(95,115+1):
    temp = ''
    j = 0
    while j < len(str(i)):
        if str(i)[j] not in temp:
            temp += str(i)[j]
            j += 1
        else:
            l = j
            h = len(temp)  
            while l + h <= len(str(i)) and str(i)[l:l+h] == temp:
                l += h
                
            if l == len(str(i)):      # reached exact end with full blocks
                invalid_ids.append(i)
                break
                    
            else:
                temp += str(i)[j]
                j += 1

print(invalid_ids)
            