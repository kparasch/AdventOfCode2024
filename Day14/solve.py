import time
import numpy as np
import matplotlib.pyplot as plt

example_file = 'example.txt'
input_file = 'input.txt'

def read_file(input_file: str) -> list[tuple[int,int,int,int]]:
    infile = open(input_file, 'r')

    robots = []
    for line in infile:
        sline = line.strip()
        pline, vline = sline.split(' ')
        pline = pline.split('=')[-1]
        vline = vline.split('=')[-1]
        px, py = tuple(map(int,pline.split(',')))
        vx, vy = tuple(map(int,vline.split(',')))
        robots.append((px, py, vx, vy))


    return robots 


def visualize_grid(grid: list[list[int]]) -> None:
    N = len(grid)
    M = len(grid[0])
    for j in range(M):
        for i in range(N):
            if grid[i][j] == 0:
                grid[i][j] = '.'
            else:
                grid[i][j] = str(grid[i][j])


    for i in range(N):
        print("".join(grid[i]))
    return


def part1(input_file: str, M: int, N: int, visualize: bool = True) -> int:
    robots = read_file(input_file)
    seconds = 100
    grid = [[0 for i in range(M)] for j in range(N)]
    for x,y,vx,vy in robots:
        new_x = (x + seconds * vx)%M
        new_y = (y + seconds * vy)%N
        grid[new_y][new_x] += 1
    
    solution = 0
    Q1, Q2, Q3, Q4 = 0, 0, 0, 0
    Q1 = sum([sum(line[:M//2]) for line in grid[:N//2]])
    Q2 = sum([sum(line[M//2+1:]) for line in grid[:N//2]])
    Q3 = sum([sum(line[:M//2]) for line in grid[N//2+1:]])
    Q4 = sum([sum(line[M//2+1:]) for line in grid[N//2+1:]])
    solution = Q1 * Q2 * Q3 * Q4

    if visualize:
        visualize_grid(grid)

    return solution 

def get_grid(robots, seconds, M, N):
    grid = [[0 for i in range(M)] for j in range(N)]
    for x,y,vx,vy in robots:
        new_x = (x + seconds * vx)%M
        new_y = (y + seconds * vy)%N
        grid[new_y][new_x] += 1
    return grid


def part2(input_file: str, M: int, N: int) -> int:
    robots = read_file(input_file)

    plt.ion()
    figure, ax = plt.subplots()
    for seconds in range(20000):
        grid = get_grid(robots, seconds, M, N)
        qq = sum([sum(line[:30]) for line in grid[:30]])
        if qq > 20: continue
        ax.clear()
        ax.pcolormesh(grid)
        ax.set_title(f'{seconds}')
        figure.canvas.draw()
        figure.canvas.flush_events()
        time.sleep(0.1)
        #print(seconds, qq)
        plt.savefig(f"frames/{seconds}.png")

    return


print(f"Day 14, Part 1 example: {part1(example_file, 11, 7, visualize=True)}")
print(f"Day 14, Part 1 solution: {part1(input_file, 101, 103, visualize=False)}")

#print(f"Day 14, Part 2 example: {part2(example_file)}")
print(f"Day 14, Part 2 solution: {part2(input_file, 101, 103)}")