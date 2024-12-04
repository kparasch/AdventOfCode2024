
example_file = 'example.txt'
example2_file = 'example2.txt'
input_file = 'input.txt'

numbers = '0123456789'

def read_file(input_file):
    infile = open(input_file, 'r')

    lines = ""
    for line in infile:
        lines = lines + line.strip()
    infile.close()
    return lines

def part1(input_file):
    lines = read_file(input_file) 

    N = len(lines)
    solution = 0
    for ii in range(N):
        if lines[ii] == 'm':
            if lines[ii+1:ii+4] == 'ul(':
                jj = 0
                number1 = ""
                while lines[ii+4+jj] in numbers:
                    number1 = number1 + lines[ii+4+jj]
                    jj += 1

                if lines[ii+4+jj] != ',':
                    continue
                
                jj += 1

                kk = 0
                number2 = ""
                while lines[ii+4+jj+kk] in numbers:
                    number2 = number2 + lines[ii+4+jj+kk]
                    kk += 1

                if lines[ii+4+jj+kk] == ')':
                    solution += int(number1) * int(number2)
    return solution
            
def part2(input_file):
    lines = read_file(input_file) 

    disabled = False

    N = len(lines)
    solution = 0
    for ii in range(N):
        if lines[ii] == 'm':
            if lines[ii+1:ii+4] == 'ul(':
                jj = 0
                number1 = ""
                while lines[ii+4+jj] in numbers:
                    number1 = number1 + lines[ii+4+jj]
                    jj += 1

                if lines[ii+4+jj] != ',':
                    continue
                
                jj += 1

                kk = 0
                number2 = ""
                while lines[ii+4+jj+kk] in numbers:
                    number2 = number2 + lines[ii+4+jj+kk]
                    kk += 1

                if lines[ii+4+jj+kk] == ')':
                    if not disabled:
                        solution += int(number1) * int(number2)
        elif lines[ii] == 'd':
            if lines[ii+1:ii+4] == 'o()':
                disabled = False
            elif lines[ii+1:ii+7] == "on't()":
                disabled = True
    return solution


print(f"Day 3, Part 1 example: {part1(example_file)}")
print(f"Day 3, Part 1 solution: {part1(input_file)}")
 
print(f"Day 3, Part 2 example: {part2(example2_file)}")
print(f"Day 3, Part 2 solution: {part2(input_file)}")