from math import gcd

example_file = 'example.txt'
input_file = 'input.txt'


def read_file(input_file: str) -> list:
    infile = open(input_file, 'r')

    grid = []
    for line in infile:
        sline = list(line.strip())
        grid.append(sline)

    return grid


def get_antennas(grid: list[list[str]]) -> dict:
    antennas = {}
    N = len(grid)
    M = len(grid[0])

    for ii in range(N):
        for jj in range(M):
            g = grid[ii][jj]
            if g != '.':
                if g in antennas.keys():
                    antennas[g].append((ii,jj))
                else:
                    antennas[g] = [(ii,jj)]
    return antennas

def get_antinodes(antennas: dict, G1: int, G2: int) -> list[tuple[int]]:
    antinodes = []
    for key in antennas.keys():
        antenna_list = antennas[key]
        N = len(antenna_list)
        for ii in range(N-1):
            for jj in range(ii+1, N):
                a1_ii, a1_jj = antenna_list[ii]
                a2_ii, a2_jj = antenna_list[jj]

                an1_ii = a1_ii - (a2_ii - a1_ii)
                an1_jj = a1_jj - (a2_jj - a1_jj)
                if an1_ii >= 0 and an1_ii < G1 and an1_jj >= 0 and an1_jj < G2:
                    antinodes.append((an1_ii, an1_jj))

                an2_ii = a2_ii - (a1_ii - a2_ii)
                an2_jj = a2_jj - (a1_jj - a2_jj)
                if an2_ii >= 0 and an2_ii < G1 and an2_jj >= 0 and an2_jj < G2:
                    antinodes.append((an2_ii, an2_jj))
    
    # remove duplicates
    return set(antinodes)

def get_antinodes2(antennas: dict, G1: int, G2: int) -> list[tuple[int]]:
    antinodes = []
    for key in antennas.keys():
        antenna_list = antennas[key]
        N = len(antenna_list)
        for ii in range(N-1):
            for jj in range(ii+1, N):
                a1_ii, a1_jj = antenna_list[ii]
                a2_ii, a2_jj = antenna_list[jj]

                D1_ii =  a2_ii - a1_ii
                D1_jj =  a2_jj - a1_jj
                gcd1 = gcd(D1_ii, D1_jj)
                D1_ii /= gcd1
                D1_jj /= gcd1

                # go up from first antenna
                an1_ii = a1_ii
                an1_jj = a1_jj
                while an1_ii >= 0 and an1_ii < G1 and an1_jj >= 0 and an1_jj < G2:
                    antinodes.append((an1_ii, an1_jj))
                    an1_ii = an1_ii + D1_ii
                    an1_jj = an1_jj + D1_jj

                # go down from first antenna
                an1_ii = a1_ii
                an1_jj = a1_jj
                while an1_ii >= 0 and an1_ii < G1 and an1_jj >= 0 and an1_jj < G2:
                    antinodes.append((an1_ii, an1_jj))
                    an1_ii = an1_ii - D1_ii
                    an1_jj = an1_jj - D1_jj
                    
    # remove duplicates
    return set(antinodes)



def part1(input_file: str) -> int:
    grid = read_file(input_file) 
    N = len(grid)
    M = len(grid[0])

    antennas = get_antennas(grid)
    antinodes = get_antinodes(antennas, N, M)
    solution = len(antinodes)

    return solution
            


def part2(input_file: str) -> int:
    grid = read_file(input_file) 
    N = len(grid)
    M = len(grid[0])

    antennas = get_antennas(grid)
    antinodes = get_antinodes2(antennas, N, M)
    solution = len(antinodes)

    return solution

print(f"Day 8, Part 1 example: {part1(example_file)}")
print(f"Day 8, Part 1 solution: {part1(input_file)}")
  
print(f"Day 8, Part 2 example: {part2(example_file)}")
print(f"Day 8, Part 2 solution: {part2(input_file)}")