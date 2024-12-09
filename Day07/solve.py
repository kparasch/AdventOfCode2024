example_file = 'example.txt'
input_file = 'input.txt'


def read_file(input_file: str) -> tuple[list, list]:
    infile = open(input_file, 'r')

    values = []
    equations = []
    for line in infile:
        val, eq = line.strip().split(':')
        val = int(val) 
        eq = list(map(int,eq.strip().split(" ")))
        values.append(val)
        equations.append(eq)
    return values, equations

def reduce_eq(original_eq: list[int], cap: int = None) -> list:
    
    results = []

    residuals = [original_eq[0]]
    equations = [original_eq[1:]]

    more_eq = True
    while more_eq:
        more_eq = False
        new_equations = []
        new_residuals = []
        for equation, res in zip(equations, residuals):
            if res > cap:
                continue
            if len(equation) != 0:
                more_eq = True
                eqp = equation.copy()
                ## op is +
                resp = eqp[0] + res
                del eqp[0]
                new_equations.append(eqp)
                new_residuals.append(resp)

                eqm = equation.copy()
                ## op is *
                resm = eqm[0] * res
                del eqm[0]
                new_equations.append(eqm)
                new_residuals.append(resm)
            else:
                results.append(res)


        equations = new_equations
        residuals = new_residuals
    return results

def reduce_eq2(original_eq: list[int], cap: int = None) -> list:
    
    results = []

    residuals = [original_eq[0]]
    equations = [original_eq[1:]]

    more_eq = True
    while more_eq:
        more_eq = False
        new_equations = []
        new_residuals = []
        for equation, res in zip(equations, residuals):
            if res > cap:
                continue
            if len(equation) != 0:
                more_eq = True
                eqp = equation.copy()
                ## op is +
                resp = eqp[0] + res
                del eqp[0]
                new_equations.append(eqp)
                new_residuals.append(resp)

                eqm = equation.copy()
                ## op is *
                resm = eqm[0] * res
                del eqm[0]
                new_equations.append(eqm)
                new_residuals.append(resm)

                eqc = equation.copy()
                ## op is ||
                resc = int(str(res) + str(eqc[0]))
                del eqc[0]
                new_equations.append(eqc)
                new_residuals.append(resc)
            else:
                results.append(res)


        equations = new_equations
        residuals = new_residuals
    return results





def part1(input_file: str) -> int:
    values, equations = read_file(input_file) 

    solution = 0
    for val, eq in zip(values, equations):
        results = reduce_eq(eq, val)
        if val in results:
            solution += val

    return solution
            


def part2(input_file: str) -> int:
    values, equations = read_file(input_file) 

    solution = 0
    for val, eq in zip(values, equations):
        results = reduce_eq2(eq, val)
        if val in results:
            solution += val
    return solution

print(f"Day 7, Part 1 example: {part1(example_file)}")
print(f"Day 7, Part 1 solution: {part1(input_file)}")
  
print(f"Day 7, Part 2 example: {part2(example_file)}")
print(f"Day 7, Part 2 solution: {part2(input_file)}")