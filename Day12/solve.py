from itertools import product
from collections import deque

example1_file = 'example1.txt'
example2_file = 'example2.txt'
input_file = 'input.txt'

def read_file(input_file: str) -> list[list]:
    infile = open(input_file, 'r')

    grid = []
    for line in infile:
        sline = list(line.strip())
        grid.append(sline)

    return grid

def lookup_area(grid: list[list]):
    area = 0
    perimeter = 0
    visited_spots = []
    queue = deque()

    N = len(grid)
    M = len(grid[0])
    for ii,jj  in product(range(N), range(M)):
        if grid[ii][jj] != 0:
            plant = grid[ii][jj]
            area += 1
            visited_spots.append((ii,jj))
            queue.append((ii,jj))
            break

    perimeter_spots = []
    while len(queue):
        ii, jj = queue.pop()
        #move up
        if ii - 1 == -1:
            perimeter += 1
            perimeter_spots.append((ii-1*N,jj))
        elif grid[ii-1][jj] != plant:
            perimeter += 1
            perimeter_spots.append((ii-1*N,jj))
        elif grid[ii-1][jj] == plant and (ii-1,jj) not in visited_spots:
            area += 1
            queue.append((ii-1,jj))
            visited_spots.append(((ii-1,jj)))

        #move down
        if ii + 1 == N:
            perimeter += 1
            perimeter_spots.append((ii+1*N,jj))
        elif grid[ii+1][jj] != plant:
            perimeter += 1
            perimeter_spots.append((ii+1*N,jj))
        elif grid[ii+1][jj] == plant and (ii+1,jj) not in visited_spots:
            area += 1
            queue.append((ii+1,jj))
            visited_spots.append((ii+1,jj))

        #move left
        if jj - 1 == -1:
            perimeter += 1
            perimeter_spots.append((ii,jj-1*M))
        elif grid[ii][jj-1] != plant:
            perimeter += 1
            perimeter_spots.append((ii,jj-1*M))
        elif grid[ii][jj-1] == plant and (ii,jj-1) not in visited_spots:
            area += 1
            queue.append((ii,jj-1))
            visited_spots.append((ii,jj-1))

        #move right
        if jj + 1 == M:
            perimeter += 1
            perimeter_spots.append((ii,jj+1*M))
        elif grid[ii][jj+1] != plant:
            perimeter += 1
            perimeter_spots.append((ii,jj+1*M))
        elif grid[ii][jj+1] == plant and (ii,jj+1) not in visited_spots:
            area += 1
            queue.append((ii,jj+1))
            visited_spots.append((ii,jj+1))

    for ii,jj in visited_spots:
        grid[ii][jj] = 0
    return area, perimeter, plant, perimeter_spots

def get_sides(perimeter_spots: list):

    sides = 0
    while len(perimeter_spots):
        neighbours = deque([perimeter_spots[0]])
        del perimeter_spots[0]
        while len(neighbours):
            sii, sjj = neighbours.pop()
            to_delete = []
            for kk in range(len(perimeter_spots)):
                ii, jj = perimeter_spots[kk]
                if abs(sii - ii) + abs(sjj - jj) == 1:
                    neighbours.append((ii, jj))
                    to_delete.append(kk)
            to_delete = sorted(to_delete)
            for kk in to_delete[::-1]:
                del perimeter_spots[kk]
        sides += 1
    return sides

    

def part1(input_file: str) -> int:
    grid = read_file(input_file)

    N = len(grid)
    M = len(grid[0])

    solution = 0

    total_area = N*M
    while total_area > 0:
        area, perimeter, plant, perimeter_spots = lookup_area(grid)
        total_area -= area
        solution += area*perimeter

    return solution 


def part2(input_file: str) -> int:
    grid = read_file(input_file)

    N = len(grid)
    M = len(grid[0])

    solution = 0

    total_area = N*M
    while total_area > 0:
        area, perimeter, plant, perimeter_spots = lookup_area(grid)
        total_area -= area
        sides = get_sides(perimeter_spots)
        solution += area*sides

    return solution 


print(f"Day 12, Part 1 example 1: {part1(example1_file)}")
print(f"Day 12, Part 1 example 2: {part1(example2_file)}")
print(f"Day 12, Part 1 solution: {part1(input_file)}")

print(f"Day 12, Part 2 example 1: {part2(example1_file)}")
print(f"Day 12, Part 2 example 2: {part2(example2_file)}")
print(f"Day 12, Part 2 solution: {part2(input_file)}")