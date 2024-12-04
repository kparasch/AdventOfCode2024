example_file = 'example.txt'
input_file = 'input.txt'

DIRECTIONS = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1, 0), (-1,1)]
XDIRECTIONS = [(1,1), (1,-1), (-1,-1), (-1,1)]

def read_file(input_file):
    infile = open(input_file, 'r')
    
    start = True
    grid = []
    for line in infile:
        if start:
            for _ in range(3):
                grid.append( ( 6 + len(line.strip()) ) * ['.'] )
            start = False
        
        grid.append(3*['.'] + list(line.strip()) + 3*['.'])

    for _ in range(3):
        grid.append( ( 6 + len(line.strip()) ) * ['.'] )
    infile.close()

    return grid

def part1(input_file):
    grid = read_file(input_file) 
    
    solution = 0

    M = len(grid)
    N = len(grid[0])

    for ii in range(3,M-3):
        for jj in range(3,N-3):
            if grid[ii][jj] == 'X':
                for di, dj in DIRECTIONS:
                    word = "".join([grid[ii + ss*di][jj + ss*dj] for ss in range(1,4)])
                    if word == 'MAS':
                        solution += 1
    return solution
            
def part2(input_file):
    grid = read_file(input_file) 
    
    solution = 0
    M = len(grid)
    N = len(grid[0])

    for ii in range(3,M-3):
        for jj in range(3,N-3):
            if grid[ii][jj] == 'A':
                for di, dj in XDIRECTIONS:
                    word = "".join([grid[ii + ss*di][jj + ss*dj] for ss in range(-1,2)])
                    if word == 'MAS':
                        dii, djj = dj, -di
                        word = "".join([grid[ii + ss*dii][jj + ss*djj] for ss in range(-1,2)])
                        if word == 'MAS':
                            solution += 1
    return solution

print(f"Day 4, Part 1 example: {part1(example_file)}")
print(f"Day 4, Part 1 solution: {part1(input_file)}")
 
print(f"Day 4, Part 2 example: {part2(example_file)}")
print(f"Day 4, Part 2 solution: {part2(input_file)}")