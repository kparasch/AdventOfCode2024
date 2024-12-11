example_file = 'example.txt'
input_file = 'input.txt'

def read_file(input_file: str) -> dict[int, int]:
    infile = open(input_file, 'r')

    for line in infile:
        list_of_stones = list(map(int,line.strip().split(" ")))
        break

    stones = {}
    for stone in list_of_stones:
        if stone in stones.keys():
            stones[stone] += 1
        else:
            stones[stone] = 1

    return stones

def add_stone(new_stones: dict[int, int], new_stone: int, number_of_stones: int) -> None:
    if new_stone in new_stones.keys():
        new_stones[new_stone] += number_of_stones
    else:
        new_stones[new_stone] = number_of_stones
    return 


def blink(stones: dict[int, int]) -> dict[int, int]:
    new_stones = {}
    for stone in stones.keys():
        if stone == 0:
            number_of_stones = stones[stone]
            add_stone(new_stones, 1, number_of_stones)

        elif len(str(stone))%2 == 0:
            number_of_stones = stones[stone]
            N = len(str(stone))//2
            add_stone(new_stones, int(str(stone)[:N]), number_of_stones)
            add_stone(new_stones, int(str(stone)[N:]), number_of_stones)
        else:
            number_of_stones = stones[stone]
            add_stone(new_stones, stone*2024, number_of_stones)
    return new_stones


def part1(input_file: str) -> int:
    stones = read_file(input_file)

    solution = 0
    for _ in range(25):
        stones = blink(stones)
    for stone in stones.keys():
        solution += stones[stone]

    return solution 


def part2(input_file: str) -> int:
    stones = read_file(input_file)

    solution = 0
    for _ in range(75):
        stones = blink(stones)
    for stone in stones.keys():
        solution += stones[stone]

    return solution 

print(f"Day 11, Part 1 example: {part1(example_file)}")
print(f"Day 11, Part 1 solution: {part1(input_file)}")

print(f"Day 11, Part 2 example: {part2(example_file)}")
print(f"Day 11, Part 2 solution: {part2(input_file)}")