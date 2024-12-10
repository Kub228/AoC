f1 = open('2024_f\\5_1.txt','r')
f2 = open('2024_f\\5_2.txt','r')

f1 = f1.read()
f2 = f2.read()

def sol1(f1, f2):
    rules = {}
    n = []
    pg = []
    total = 0
    
    for i in range(len(f1)):
        if f1[i].isdigit():
            n.append(f1[i])
        
        if not f1[i].isdigit():
            if n:
                x = ''.join(n)
                pg.append(x)
                n = []
                
            if len(pg) == 2:
                if int(pg[0]) not in rules:
                    rules[int(pg[0])] = []
                rules[int(pg[0])].append(int(pg[1]))
                pg = []
    
    n = []
    pg_o = []
    
    for i in range(len(f2)):
        if f2[i].isdigit():
            n.append(f2[i])
            
        if not f2[i].isdigit():
            if n:
                x = ''.join(n)
                pg_o.append(int(x))
                n = []
            
            if f2[i] == '\n':
                # Check if this update is in correct order
                valid = True
                for i in range(len(pg_o)):
                    for j in range(i + 1, len(pg_o)):
                        if pg_o[j] in rules and pg_o[i] in rules[pg_o[j]]:
                            valid = False
                            break
                    if not valid:
                        break
                
                if valid and len(pg_o) % 2 != 0:
                    mid = len(pg_o) // 2
                    total += pg_o[mid]
                pg_o = []
    
    return total

def sol2(f1, f2):
    rules = {}
    n = []
    pg = []
    total = 0
    
    for i in range(len(f1)):
        if f1[i].isdigit():
            n.append(f1[i])
        
        if not f1[i].isdigit():
            if n:
                x = ''.join(n)
                pg.append(x)
                n = []
                
            if len(pg) == 2:
                if int(pg[0]) not in rules:
                    rules[int(pg[0])] = []
                rules[int(pg[0])].append(int(pg[1]))
                pg = []
    
    n = []
    pg_o = []
    
    for i in range(len(f2)):
        if f2[i].isdigit():
            n.append(f2[i])
            
        if not f2[i].isdigit():
            if n:
                x = ''.join(n)
                pg_o.append(int(x))
                n = []
            
            if f2[i] == '\n':
                # Check if this update is in correct order
                valid = True
                for i in range(len(pg_o)):
                    for j in range(i + 1, len(pg_o)):
                        if pg_o[j] in rules and pg_o[i] in rules[pg_o[j]]:
                            valid = False
                            break
                    if not valid:
                        break
                
                if not valid: 
                    
                    # Perform topological sort for reordering
                    from collections import defaultdict, deque
                    
                    # Build graph
                    graph = defaultdict(list)
                    in_degree = defaultdict(int)
                    nodes = set(pg_o)
                    
                    # Add all nodes first
                    for node in pg_o:
                        if node not in graph:
                            graph[node] = []
                    
                    # Add edges from rules
                    for node in nodes:
                        if node in rules:
                            for next_node in rules[node]:
                                if next_node in nodes:
                                    graph[node].append(next_node)
                                    in_degree[next_node] += 1
                    
                    # Topological sort
                    queue = deque([node for node in nodes if in_degree[node] == 0])
                    ordered = []
                    
                    while queue:
                        current = queue.popleft()
                        ordered.append(current)
                        for neighbor in graph[current]:
                            in_degree[neighbor] -= 1
                            if in_degree[neighbor] == 0:
                                queue.append(neighbor)
                    
                    # Only add to total if we have all nodes in ordered result
                    if len(ordered) == len(pg_o) and len(ordered) % 2 != 0:
                        mid = len(ordered) // 2
                        total += ordered[mid]
                pg_o = []
    
    return total
    
    

print(sol1(f1,f2))
print(sol2(f1,f2))