import numpy as np

example_file = 'example.txt'
input_file = 'input.txt'


def read_file(input_file):
    infile = open(input_file, 'r')

    reports = []
    for line in infile:
        report = list(map(int,line.strip().split()))
        reports.append(report)
    infile.close()
    return reports

def is_safe(report):
    diff = np.diff(report)
    condition1 = np.all(diff > 0) or np.all(diff < 0)
    adiff = np.abs(diff)
    condition2 = np.max(adiff) <= 3 and np.min(adiff >= 1)
    return condition1 and condition2

def part1(input_file):
    reports = read_file(input_file) 

    number_of_safes = 0
    for report in reports:
        if is_safe(report):
            number_of_safes += 1
    
    return number_of_safes


def part2(input_file):
    reports = read_file(input_file) 

    number_of_safes = 0
    for report in reports:
        if is_safe(report):
            number_of_safes += 1
        else:
            for ii in range(len(report)):
                new_report = report[:ii] + report[ii+1:]
                if is_safe(new_report):
                    number_of_safes += 1
                    break
    return number_of_safes



print(f"Day 2, Part 1 example: {part1(example_file)}")
print(f"Day 2, Part 1 solution: {part1(input_file)}")
 
print(f"Day 2, Part 2 example: {part2(example_file)}")
print(f"Day 2, Part 2 solution: {part2(input_file)}")