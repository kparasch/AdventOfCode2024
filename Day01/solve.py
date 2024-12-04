from collections import Counter

example_file = 'example.txt'
input_file = 'input.txt'



def part1(input_file):
    infile = open(input_file, 'r')
    first_list = []
    second_list = []
    
    for line in infile:
        one, two = line.strip().split('   ')
        first_list.append(int(one))
        second_list.append(int(two))
    
    sorted_first_list = sorted(first_list)
    sorted_second_list = sorted(second_list)
    
    distances = []
    for ii in range(len(sorted_first_list)):
        distances.append(abs(sorted_second_list[ii] - sorted_first_list[ii]))
    
    solution = sum(distances)
    return solution


def part2(input_file):
    infile = open(input_file, 'r')
    first_list = []
    second_list = []
    
    for line in infile:
        one, two = line.strip().split('   ')
        first_list.append(int(one))
        second_list.append(int(two))
    
    counter = Counter(second_list)

    scores = []
    for ii in first_list:
        scores.append(ii*counter[ii])
    
    solution = sum(scores) 
    return solution


print(f"Day 1, Part 1 example: {part1(example_file)}")
print(f"Day 1, Part 1 solution: {part1(input_file)}")

print(f"Day 1, Part 2 example: {part2(example_file)}")
print(f"Day 1, Part 2 solution: {part2(input_file)}")