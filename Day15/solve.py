import numpy as np

example_file = 'example.txt'
example2_file = 'example2.txt'
input_file = 'input.txt'


def read_file(input_file: str) -> tuple[np.array, list]:
    infile = open(input_file, 'r')

    grid = []
    moves = []
    gridding = True
    for line in infile:
        sline = list(line.strip())
        if not len(sline):
            gridding = False
            continue
        if gridding:
            grid.append(sline)
        if not gridding:
            moves = moves + list(sline)

    return np.array(grid), moves

def read_file2(input_file: str) -> tuple[np.array, list]:
    infile = open(input_file, 'r')

    grid = []
    moves = []
    gridding = True
    for line in infile:
        sline = list(line.strip())
        if not len(sline):
            gridding = False
            continue
        if gridding:
            new_line = []
            for ch in sline:
                if ch == '#':
                    new_line.append('#')
                    new_line.append('#')
                elif ch == 'O':
                    new_line.append('[')
                    new_line.append(']')
                elif ch == '.':
                    new_line.append('.')
                    new_line.append('.')
                elif ch == '@':
                    new_line.append('@')
                    new_line.append('.')
            grid.append(new_line)
        if not gridding:
            moves = moves + list(sline)

    return np.array(grid), moves


def part1(input_file: str) -> int:
    grid, moves = read_file(input_file)

    N, M = grid.shape

    robot_i, robot_j = np.where(grid=='@')
    robot_i = robot_i[0]
    robot_j = robot_j[0]

    for move in moves:
        if move == '^':
            di, dj = -1, 0
        elif move == 'v':
            di, dj = +1, 0
        elif move == '<':
            di, dj = 0, -1
        elif move == '>':
            di, dj = 0, +1
        else:
            raise Exception('Unknown move')
        next_i = robot_i + di
        next_j = robot_j + dj
        while grid[next_i, next_j] == 'O':
            next_i += di
            next_j += dj
        if grid[next_i, next_j] == '.':
            if di == 0:
                j1 = min(next_j, robot_j)
                j2 = max(next_j, robot_j)
                if dj < 0:
                    grid[robot_i, j1:j2] = grid[robot_i, j1-dj:j2-dj]
                else:
                    grid[robot_i, j1+dj:j2+dj] = grid[robot_i, j1:j2]
                grid[robot_i, robot_j] = '.' 
            elif dj == 0:
                i1 = min(next_i, robot_i)
                i2 = max(next_i, robot_i)
                if di < 0:
                    grid[i1:i2, robot_j] = grid[i1-di:i2-di, robot_j]
                else:
                    grid[i1+di:i2+di, robot_j] = grid[i1:i2, robot_j]
                grid[robot_i, robot_j] = '.'
            robot_i += di
            robot_j += dj
    
    solution = 0
    for i in range(N):
        for j in range(M):
            if grid[i,j] == 'O':
                solution += 100*i + j

    return solution 

def print_grid(grid):
    N, M = grid.shape
    for i in range(N):
        print("".join(grid[i]))
    return
    

def part2(input_file: str) -> int:
    grid, moves = read_file2(input_file)

    #print_grid(grid)
    N, M = grid.shape

    robot_i, robot_j = np.where(grid=='@')
    robot_i = robot_i[0]
    robot_j = robot_j[0]

    for move in moves:
        if move == '^':
            di, dj = -1, 0
        elif move == 'v':
            di, dj = +1, 0
        elif move == '<':
            di, dj = 0, -1
        elif move == '>':
            di, dj = 0, +1
        else:
            raise Exception('Unknown move')
        
        if di == 0:
            next_i = robot_i + di
            next_j = robot_j + dj
            while grid[next_i, next_j] in ['[',']'] :
                next_i += di
                next_j += dj
            if grid[next_i, next_j] == '.':
                j1 = min(next_j, robot_j)
                j2 = max(next_j, robot_j)
                if dj < 0:
                    grid[robot_i, j1:j2] = grid[robot_i, j1-dj:j2-dj]
                else:
                    grid[robot_i, j1+dj:j2+dj] = grid[robot_i, j1:j2]
                grid[robot_i, robot_j] = '.' 
                robot_i += di
                robot_j += dj
        else:
            next_i = robot_i + di
            next_j = robot_j + dj
            if grid[next_i, next_j] == '.':
                i1 = min(next_i, robot_i)
                i2 = max(next_i, robot_i)
                if di < 0:
                    grid[i1:i2, robot_j] = grid[i1-di:i2-di, robot_j]
                else:
                    grid[i1+di:i2+di, robot_j] = grid[i1:i2, robot_j]
                grid[robot_i, robot_j] = '.' 
                robot_i += di
                robot_j += dj

            elif grid[next_i, next_j] in ['[',']']:
                boxes = []
                if grid[next_i, next_j] == '[':
                    edges = [(next_i + di, next_j), (next_i + di, next_j + 1)]
                    boxes.append((next_i, next_j))
                    boxes.append((next_i, next_j+1))
                elif grid[next_i, next_j] == ']':
                    edges = [(next_i + di, next_j), (next_i + di, next_j - 1)]
                    boxes.append((next_i, next_j))
                    boxes.append((next_i, next_j-1))
                
                all_edges_good = False
                do_not_move = False
                while not all_edges_good:
                    new_edges = []
                    all_edges_good = True
                    for ei,ej in edges:
                        #breakpoint()
                        if grid[ei,ej] == '.':
                            new_edges.append((ei, ej))
                            #pass
                        elif grid[ei,ej] == '[':
                            if grid[ei-di,ej] == '[':
                                new_edges.append((ei+di, ej))
                                boxes.append((ei, ej))
                            else:
                                new_edges.append((ei+di, ej))
                                new_edges.append((ei+di, ej+1))
                                boxes.append((ei, ej))
                                boxes.append((ei, ej+1))
                            all_edges_good = False
                        elif grid[ei,ej] == ']':
                            if grid[ei-di,ej] == ']':
                                new_edges.append((ei+di, ej))
                                boxes.append((ei, ej))
                            else:
                                new_edges.append((ei+di, ej))
                                new_edges.append((ei+di, ej-1))
                                boxes.append((ei, ej))
                                boxes.append((ei, ej-1))
                            all_edges_good = False
                        elif grid[ei,ej] == '#':
                            do_not_move = True
                            break
                    edges = new_edges
                if do_not_move:
                    continue
                else:
                    boxes = list(set(boxes))
                    while len(boxes) > 0:
                        if di < 0:
                            indices = []
                            min_pos = len(grid)
                            for kk in range(len(boxes)):
                                bi, bj = boxes[kk]
                                if bi < min_pos:
                                    indices = [kk]
                                    min_pos = bi
                                elif bi == min_pos:
                                    indices.append(kk)

                            indices = sorted(indices)[::-1]
                            for index in indices:
                                bi, bj = boxes[index]
                                grid[bi+di,bj] = grid[bi,bj]
                                grid[bi,bj] = '.'
                                del boxes[index]

                        elif di > 0:
                            indices = []
                            max_pos = 0
                            for kk in range(len(boxes)):
                                bi, bj = boxes[kk]
                                if bi > max_pos:
                                    indices = [kk]
                                    max_pos = bi
                                elif bi == max_pos:
                                    indices.append(kk)

                            indices = sorted(indices)[::-1]
                            for index in indices:
                                bi, bj = boxes[index]
                                grid[bi+di,bj] = grid[bi,bj]
                                grid[bi,bj] = '.'
                                del boxes[index]
                    grid[robot_i+di, robot_j] = grid[robot_i, robot_j]
                    grid[robot_i, robot_j] = '.' 
                    robot_i += di
                    robot_j += dj

        #print_grid(grid)

    solution = 0
    for i in range(N):
        for j in range(M):
            if grid[i,j] == '[':
                solution += 100*i + j

    return solution


print(f"Day 15, Part 1 example: {part1(example_file)}")
print(f"Day 15, Part 1 solution: {part1(input_file)}")

print(f"Day 15, Part 2 example 2: {part2(example2_file)}")
print(f"Day 15, Part 2 example: {part2(example_file)}")
print(f"Day 15, Part 2 solution: {part2(input_file)}")