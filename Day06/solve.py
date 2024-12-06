example_file = 'example.txt'
input_file = 'input.txt'


def read_file(input_file: str) -> list:
    infile = open(input_file, 'r')

    grid = []
    for line in infile:
        sline = list(line.strip())
        grid.append(sline)

    return grid

def loop(grid: list, ii_guard: int, jj_guard: int, di: int, dj: int) -> bool:
    N = len(grid)
    M = len(grid[0])

    stuck = False

    obstructions = {}
    while True:
        next_ii = ii_guard + di
        next_jj = jj_guard + dj
        if next_ii >= N or next_ii < 0 or next_jj >= M or next_jj < 0:
            break
        elif grid[next_ii][next_jj] in ['.', 'X', '^']:
            grid[next_ii][next_jj] = 'X'
            ii_guard = next_ii
            jj_guard = next_jj
        elif grid[next_ii][next_jj] in ['#', 'O']:
            di, dj = dj, -di
            key = (next_ii, next_jj)
            if key in obstructions.keys():
                obstructions[key] += 1
                if obstructions[key] > 4:
                    stuck = True
                    break
            else:
                obstructions[key] = 1


    return stuck

def part1(input_file: str) -> int:
    grid = read_file(input_file) 
    N = len(grid)
    M = len(grid[0])

    # find initial position
    for ii in range(N):
        for jj in range(M):
            if grid[ii][jj] == '^':
                ii_guard = ii
                jj_guard = jj
                break
    
    di = -1
    dj = 0
    _ = loop(grid, ii_guard, jj_guard, di, dj)
    
    solution = 0
    for line in grid:
        for gg in line:
            if gg in ['^', 'X']:
                solution += 1

    return solution
            


def part2(input_file: str) -> int:
    grid = read_file(input_file) 
    N = len(grid)
    M = len(grid[0])

    # find initial position
    for ii in range(N):
        for jj in range(M):
            if grid[ii][jj] == '^':
                ii_guard = ii
                jj_guard = jj
                break
    
    viable_obstructions = {}
    di = -1
    dj = 0
    while True:
        next_ii = ii_guard + di
        next_jj = jj_guard + dj
        if next_ii >= N or next_ii < 0 or next_jj >= M or next_jj < 0:
            break
        elif grid[next_ii][next_jj] in ['.', 'X', '^']:
            if grid[next_ii][next_jj] not in ['^', 'X']:
                temp_grid = [line.copy() for line in grid]
                temp_grid[next_ii][next_jj] = 'O'
                stuck = loop(temp_grid, ii_guard, jj_guard, di, dj)
                if stuck:
                    if (next_ii, next_jj) in viable_obstructions.keys():
                        viable_obstructions[(next_ii, next_jj)] += 1
                    else:
                        viable_obstructions[(next_ii, next_jj)] = 1
                grid[next_ii][next_jj] = 'X'
            ii_guard = next_ii
            jj_guard = next_jj
        elif grid[next_ii][next_jj] == "#":
            di, dj = dj, -di
    
    solution = len(viable_obstructions.keys())
    return solution

print(f"Day 6, Part 1 example: {part1(example_file)}")
print(f"Day 6, Part 1 solution: {part1(input_file)}")
  
print(f"Day 6, Part 2 example: {part2(example_file)}")
print(f"Day 6, Part 2 solution: {part2(input_file)}")