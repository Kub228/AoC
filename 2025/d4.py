inpt =   '''..@@.@@@@.
            @@@.@.@.@@
            @@@@@.@.@@
            @.@@@@..@.
            @@.@@@@.@@
            .@@@@@@@.@
            .@.@.@.@@@
            @.@@@.@@@@
            .@@@@@@@@.
            @.@.@@@.@.'''.split()

# with open("txt_files\\d4.txt") as f:
#   inpt = f.read().split()

inpt = [list(i) for i in inpt]

ans = 0

offsets = [(-1, -1), (-1, 0), (-1, 1),
           (0, -1),           (0, 1),
           (1, -1),  (1, 0),  (1, 1)]

rows = len(inpt)
cols = len(inpt[0])
while True:
    modified = False
    for i in range(rows):
        for j in range(cols):
            if inpt[i][j] == '@':
                nbrs = []
                for dx, dy in offsets:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < rows and 0 <= nj < cols:
                        nbrs.append(inpt[ni][nj])

                temp = nbrs.count('@')
                if temp < 4:
                    inpt[i][j] = 'x'
                    modified = True
    
    if modified == False:
        break
    ans += 1


print(ans)