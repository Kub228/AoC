f = open("2024_f\\1.txt","r")

f_r=f.read()

w_f=[]
counter=1

n1=[]
l1=[]

n2=[]
l2=[]

for i in f_r:
    if ' ' in i or '\n' in i:
        counter+=1
        if '\n' in i:
            temp_n1 = ''.join(n1)
            temp_n2 = ''.join(n2)
            
            temp_n1 = int(temp_n1)
            temp_n2 = int(temp_n2)
            
            l1.append(temp_n1)
            l2.append(temp_n2)
            
            n1 = []
            n2 = []
            
            l1.sort()
            l2.sort()
    
    if ' ' not in i and '\n' not in i:        
        if counter%2!=0:
            n1.append(i)
            
        if counter%2==0:
            n2.append(i)
            

l=[]

for i in range(len(l2)):
    
    
    n=l2[i]-l1[i]
    n=abs(n)
    l.append(n)
    
print(sum(l))

        
    