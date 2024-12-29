from itertools import product

example_file = 'example.txt'
input_file = 'input.txt'

def read_file(input_file: str) -> list[list]:
    infile = open(input_file, 'r')

    grid = []
    for line in infile:
        sline = list(line.strip())
        grid.append(sline)

    return grid


def find(grid: list[list], target: str) -> tuple[int]:
    N = len(grid)
    M = len(grid[0])
    
    for i,j  in product(range(N), range(M)):
        if grid[i][j] == target:
            break
    return i, j


def part1(input_file: str) -> int:
    grid = read_file(input_file)

    N = len(grid)
    M = len(grid[0])

    start_i, start_j = find(grid, 'S')
    end_i, end_j = find(grid, 'E')
    di = 0
    dj = 1

    scores = {}
    scores[(start_i, start_j, di, dj)] = 0
    endpoints = [(start_i, start_j, di, dj)]
    while len(endpoints):
        new_endpoints = []
        for endpoint in endpoints:
            myi, myj, di, dj = endpoint
            myscore = scores[endpoint]

            #try move forward
            new_i = myi + di
            new_j = myj + dj
            new_di = di
            new_dj = dj
            if grid[new_i][new_j] != '#':
                new_endpoint = (new_i, new_j, new_di, new_dj)
                new_score = myscore + 1
                if new_endpoint in scores.keys():
                    if new_score < scores[new_endpoint]:
                        scores[new_endpoint] = new_score
                        new_endpoints.append(new_endpoint)
                else:
                    scores[new_endpoint] = new_score
                    new_endpoints.append(new_endpoint)

            #try rotate counter-clockwise
            new_i = myi
            new_j = myj
            new_di, new_dj = -dj, di
            if grid[new_i][new_j] != '#':
                new_endpoint = (new_i, new_j, new_di, new_dj)
                new_score = myscore + 1000
                if new_endpoint in scores.keys():
                    if new_score < scores[new_endpoint]:
                        scores[new_endpoint] = new_score
                        new_endpoints.append(new_endpoint)
                else:
                    scores[new_endpoint] = new_score
                    new_endpoints.append(new_endpoint)

            #try rotate clockwise
            new_i = myi
            new_j = myj
            new_di, new_dj = dj, -di
            if grid[new_i][new_j] != '#':
                new_endpoint = (new_i, new_j, new_di, new_dj)
                new_score = myscore + 1000
                if new_endpoint in scores.keys():
                    if new_score < scores[new_endpoint]:
                        scores[new_endpoint] = new_score
                        new_endpoints.append(new_endpoint)
                else:
                    scores[new_endpoint] = new_score
                    new_endpoints.append(new_endpoint)
            
            endpoints = new_endpoints
        #print(len(endpoints))

    
    solution = 999999999
    end_states = [(end_i, end_j, 1, 0),
                  (end_i, end_j, -1, 0),
                  (end_i, end_j, 0, 1),
                  (end_i, end_j, 0, -1)]

    for es in end_states:
        if scores[es] < solution:
            solution = scores[es]
    return solution 

def clean_history(new_history):
    cleaning=True
    while cleaning:
        cleaning = False
        for ii in range(len(new_history)-1):
            to_break = False
            for jj in range(ii+1, len(new_history)):
                if new_history[ii] == new_history[jj]:
                    cleaning = True
                    del new_history[jj]
                    to_break = True
                    break
            if to_break:
                break
    return new_history


def part2(input_file: str) -> int:
    grid = read_file(input_file)

    start_i, start_j = find(grid, 'S')
    end_i, end_j = find(grid, 'E')
    di = 0
    dj = 1

    history = {}

    scores = {}
    scores[(start_i, start_j, di, dj)] = 0
    endpoints = [(start_i, start_j, di, dj)]

    history[(start_i, start_j, di, dj)] = [[(start_i, start_j)]]

    while len(endpoints):
        new_endpoints = []
        for endpoint in endpoints:
            myi, myj, di, dj = endpoint
            myscore = scores[endpoint]
            myhistory = history[endpoint]

            #try move forward
            new_i = myi + di
            new_j = myj + dj
            new_di = di
            new_dj = dj
            if grid[new_i][new_j] != '#':
                new_endpoint = (new_i, new_j, new_di, new_dj)
                new_score = myscore + 1
                new_history = []
                for hh in myhistory:
                    new_history.append(hh.copy())
                    new_history[-1].append((new_i, new_j))
                new_history = clean_history(new_history)

                if new_endpoint in scores.keys():
                    if new_score < scores[new_endpoint]:
                        scores[new_endpoint] = new_score
                        new_endpoints.append(new_endpoint)
                        history[new_endpoint] = new_history
                    elif new_score == scores[new_endpoint]:
                        scores[new_endpoint] = new_score
                        new_endpoints.append(new_endpoint)
                        history_to_replace = history[new_endpoint] + new_history
                        history_to_replace = clean_history(history_to_replace)
                        history[new_endpoint] = history_to_replace
                else:
                    scores[new_endpoint] = new_score
                    new_endpoints.append(new_endpoint)
                    history[new_endpoint] = new_history

            #try rotate counter-clockwise
            new_i = myi
            new_j = myj
            new_di, new_dj = -dj, di
            if grid[new_i][new_j] != '#':
                new_endpoint = (new_i, new_j, new_di, new_dj)
                new_score = myscore + 1000
                new_history = []
                for hh in myhistory:
                    new_history.append(hh.copy())
                    new_history[-1].append((new_i, new_j))
                new_history = clean_history(new_history)

                if new_endpoint in scores.keys():
                    if new_score < scores[new_endpoint]:
                        scores[new_endpoint] = new_score
                        new_endpoints.append(new_endpoint)
                        history[new_endpoint] = new_history
                    elif new_score == scores[new_endpoint]:
                        scores[new_endpoint] = new_score
                        new_endpoints.append(new_endpoint)
                        history_to_replace = history[new_endpoint] + new_history
                        history_to_replace = clean_history(history_to_replace)
                        history[new_endpoint] = history_to_replace
                else:
                    scores[new_endpoint] = new_score
                    new_endpoints.append(new_endpoint)
                    history[new_endpoint] = new_history

            #try rotate clockwise
            new_i = myi
            new_j = myj
            new_di, new_dj = dj, -di
            if grid[new_i][new_j] != '#':
                new_endpoint = (new_i, new_j, new_di, new_dj)
                new_score = myscore + 1000
                new_history = []
                for hh in myhistory:
                    new_history.append(hh.copy())
                    new_history[-1].append((new_i, new_j))
                new_history = clean_history(new_history)

                if new_endpoint in scores.keys():
                    if new_score < scores[new_endpoint]:
                        scores[new_endpoint] = new_score
                        new_endpoints.append(new_endpoint)
                        history[new_endpoint] = new_history
                    elif new_score == scores[new_endpoint]:
                        scores[new_endpoint] = new_score
                        new_endpoints.append(new_endpoint)
                        history_to_replace = history[new_endpoint] + new_history
                        history_to_replace = clean_history(history_to_replace)
                        history[new_endpoint] = history_to_replace
                else:
                    scores[new_endpoint] = new_score
                    new_endpoints.append(new_endpoint)
                    history[new_endpoint] = new_history
            
            endpoints = new_endpoints

        print(len(endpoints))

    min_score = 999999999
    end_states = [(end_i, end_j, 1, 0),
                  (end_i, end_j, -1, 0),
                  (end_i, end_j, 0, 1),
                  (end_i, end_j, 0, -1)]

    for es in end_states:
        if scores[es] < min_score:
            min_score = scores[es]
    
    best_tiles = {}
    for es in end_states:
        if scores[es] == min_score:
            for myhistory in history[es]:
                for tile in myhistory:
                    if tile in best_tiles.keys():
                        best_tiles[tile] += 1
                    else:
                        best_tiles[tile] = 1

    solution = len(best_tiles)          

    return solution


print(f"Day 16, Part 1 example: {part1(example_file)}")
print(f"Day 16, Part 1 solution: {part1(input_file)}")

print(f"Day 16, Part 2 example: {part2(example_file)}")
print(f"Day 16, Part 2 solution: {part2(input_file)}")