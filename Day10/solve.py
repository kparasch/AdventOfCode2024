from collections import deque

example_file = 'example.txt'
input_file = 'input.txt'



def read_file(input_file: str) -> list[list[int]]:
    infile = open(input_file, 'r')

    grid = []
    for line in infile:
        gline = list(map(int,line.strip()))
        grid.append(gline)

    return grid

def find_zeros(grid: list) -> set[tuple[int]]:
    N = len(grid)
    M = len(grid[0])

    zeros = set() 
    for ii in range(N):
        for jj in range(M):
            if grid[ii][jj] == 0:
                zeros.add((ii,jj))

    return zeros

def add_to_ways(new_ways: dict, increment: int, pp: tuple[int]) -> None:
    if pp not in new_ways.keys():
        new_ways[pp] = increment
    else:
        new_ways[pp] += increment
    return


def iterate(grid: list, positions: set[tuple[int]], target: int, ways: dict=None) -> set[tuple[int]]:
    N = len(grid)
    M = len(grid[0])

    new_positions = set()
    new_ways = dict()

    for ii, jj in positions:
        if ii < N - 1  and grid[ii+1][jj] == target:
            pp = (ii+1, jj)
            new_positions.add(pp)
            add_to_ways(new_ways, ways[(ii,jj)], pp)
        if jj < M - 1 and grid[ii][jj+1] == target:
            pp = (ii, jj+1)
            new_positions.add(pp)
            add_to_ways(new_ways, ways[(ii,jj)], pp)
        if ii > 0 and grid[ii-1][jj] == target:
            pp = (ii-1,jj)
            new_positions.add(pp)
            add_to_ways(new_ways, ways[(ii,jj)], pp)
        if jj > 0 and grid[ii][jj-1] == target:
            pp = (ii,jj-1)
            new_positions.add(pp)
            add_to_ways(new_ways, ways[(ii,jj)], pp)

    return new_positions, new_ways


def part1(input_file: str) -> int:
    grid = read_file(input_file)

    solution = 0
    positions = find_zeros(grid)
    for starting_zero in positions:
        trail = [starting_zero]
        ways = {starting_zero: 1}
        for ii in range(1,10):
            trail, ways = iterate(grid, trail, ii, ways)
        solution += len(trail)

    return solution 


def part2(input_file: str) -> int:
    grid = read_file(input_file)

    solution = 0
    positions = find_zeros(grid)
    for starting_zero in positions:
        trail = [starting_zero]
        ways = {starting_zero: 1}
        for ii in range(1,10):
            trail, ways = iterate(grid, trail, ii, ways)
        solution += sum(ways.values())
    return solution 

print(f"Day 10, Part 1 example: {part1(example_file)}")
print(f"Day 10, Part 1 solution: {part1(input_file)}")

print(f"Day 10, Part 2 example: {part2(example_file)}")
print(f"Day 10, Part 2 solution: {part2(input_file)}")