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

with open("AoC\\2025\\txt_files\\d4.txt") as f:
  inpt = f.read().split()

inpt = [list(i) for i in inpt]

ans = 0

offsets = [(-1, -1), (-1, 0), (-1, 1),
           (0, -1),           (0, 1),
           (1, -1),  (1, 0),  (1, 1)]

rows = len(inpt)
cols = len(inpt[0])

while True:
    to_change = [] 
    for i in range(rows):
        for j in range(cols):
            if inpt[i][j] == '@':
                nbrs = []
                for dx, dy in offsets:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < rows and 0 <= nj < cols:
                        nbrs.append(inpt[ni][nj])
                if nbrs.count('@') < 4:
                    to_change.append((i, j))
    if not to_change:
        break
    for i, j in to_change:
        inpt[i][j] = 'x'
    ans += len(to_change)

print(ans)