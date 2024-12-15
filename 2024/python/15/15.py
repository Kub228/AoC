def sol1():
    file = open("AoC\\2024\\files_txt\\15.txt", "r").read()
    grid = [[char for char in line] for line in file.split("\n\n")[0].split("\n")]
    sequence = "".join(file.split("\n\n")[1].strip().split("\n"))

    DIRECTIONS = {
        "<": (0, -1),
        ">": (0, 1),
        "^": (-1, 0),
        "v": (1, 0),
    }

    def robot_pos(grid):
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "@":
                    return row, col
        raise ValueError("No robot found")

    def find_box(grid):
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "O":
                    yield row, col

    def approved(grid, row, col):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != "#"

    def is_movable(grid, row, col, dr, dc, seen):
        if (row, col) in seen:
            return True
        seen.add((row, col))

        nr, nc = row + dr, col + dc
        match grid[nr][nc]:
            case "#":
                return False
            case "[":
                return is_movable(grid, nr, nc, dr, dc, seen) and is_movable(
                    grid, nr, nc + 1, dr, dc, seen
                )
            case "]":
                return is_movable(grid, nr, nc, dr, dc, seen) and is_movable(
                    grid, nr, nc - 1, dr, dc, seen
                )
            case "O":
                return is_movable(grid, nr, nc, dr, dc, seen)
        return True

    def move(grid, row, col, move):
        dr, dc = DIRECTIONS[move]

        nr, nc = row + dr, col + dc

        if not approved(grid, nr, nc):
            return row, col

        if grid[nr][nc] == "O":
            seen = set()

            if not is_movable(grid, row, col, dr, dc, seen):
                return row, col

            while len(seen) > 0:
                for r, c in seen.copy():
                    nr2, nc2 = r + dr, c + dc
                    if (nr2, nc2) not in seen:
                        if grid[r][c] != "@":
                            grid[nr2][nc2] = grid[r][c]
                            grid[r][c] = "."

                        seen.remove((r, c))

            grid[row][col], grid[nr][nc] = grid[nr][nc], grid[row][col]
            return nr, nc

        grid[row][col], grid[nr][nc] = grid[nr][nc], grid[row][col]
        return nr, nc

    row, col = robot_pos(grid)
    for move_dir in sequence:
        row, col = move(grid, row, col, move_dir)

    total = sum(100 * box[0] + box[1] for box in find_box(grid))
    
    print(f'Total: {total}')
    
def sol2():
    file = open("AoC\\2024\\files_txt\\15.txt", "r").read()
    small_grid = [[char for char in line] for line in file.split("\n\n")[0].split("\n")]
    sequence = "".join(file.split("\n\n")[1].strip().split("\n"))
    
    grid = []
    for row in small_grid:
        new_row = []
        for char in row:
            if char == "#":
                new_row.extend(["#", "#"])
            elif char == "O":
                new_row.extend(["[", "]"])
            elif char == ".":
                new_row.extend([".", "."])
            elif char == "@":
                new_row.extend(["@", "."])
        grid.append(new_row)

    DIRECTIONS = {
        "<": (0, -1),
        ">": (0, 1),
        "^": (-1, 0),
        "v": (1, 0),
    }

    def robot_pos(grid):
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "@":
                    return row, col
        raise ValueError("No robot found")

    def find_box(grid):
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "[":
                    yield row, col

    def approved(grid, row, col):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != "#"

    def is_movable(grid, row, col, dr, dc, seen):
        if (row, col) in seen:
            return True
        seen.add((row, col))

        nr, nc = row + dr, col + dc
        match grid[nr][nc]:
            case "#":
                return False
            case "[":
                return is_movable(grid, nr, nc, dr, dc, seen) and is_movable(
                    grid, nr, nc + 1, dr, dc, seen
                )
            case "]":
                return is_movable(grid, nr, nc, dr, dc, seen) and is_movable(
                    grid, nr, nc - 1, dr, dc, seen
                )
            case "O":
                return is_movable(grid, nr, nc, dr, dc, seen)
        return True

    def move(grid, row, col, move):
        dr, dc = DIRECTIONS[move]
        nr, nc = row + dr, col + dc

        if not approved(grid, nr, nc):
            return row, col

        if grid[nr][nc] in ["[", "]"]:
            seen = set()
            if not is_movable(grid, row, col, dr, dc, seen):
                return row, col

            while len(seen) > 0:
                for r, c in seen.copy():
                    nr2, nc2 = r + dr, c + dc
                    if (nr2, nc2) not in seen:
                        if grid[nr2][nc2] != "@" and grid[r][c] != "@":
                            grid[nr2][nc2] = grid[r][c]
                            grid[r][c] = "."
                        seen.remove((r, c))

            grid[row][col], grid[nr][nc] = grid[nr][nc], grid[row][col]
            return nr, nc

        grid[row][col], grid[nr][nc] = grid[nr][nc], grid[row][col]
        return nr, nc

    row, col = robot_pos(grid)
    for move_dir in sequence:
        row, col = move(grid, row, col, move_dir)

    total = sum(100 * box[0] + box[1] for box in find_box(grid))
    
    print(f'Total: {total}')

sol1()
sol2()
