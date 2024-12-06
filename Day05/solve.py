example_file = 'example.txt'
input_file = 'input.txt'


def read_file(input_file):
    infile = open(input_file, 'r')

    reading_rules = True
    rules = {}
    #rules2 = []
    updates = []
    for line in infile:
        sline = line.strip()
        if len(sline) == 0:
            reading_rules = False
            continue

        if reading_rules:
            r1, r2 = map(int,sline.split('|'))
            if r1 in rules.keys():
                rules[r1].append(r2)
            else:
                rules[r1] = [r2]
        else:
            updates.append(list(map(int,sline.split(','))))

    return rules, updates

def part1(input_file):
    rules, updates= read_file(input_file) 
    violated_updates = []
    rules1 = rules.keys()
    solution = 0
    for update in updates:
        violated = False
        for ii in range(len(update)):
            if violated:
                continue
            if update[ii] in rules1:
                for jj in range(ii):
                    if update[jj] in rules[update[ii]]:
                        violated_updates.append(update)
                        violated = True
                        break
        if not violated:
            solution += update[len(update)//2]

    return solution, violated_updates
            
def part2(input_file):
    rules, updates= read_file(input_file) 
    _, violated_updates = part1(input_file)

    solution = 0
    for update in violated_updates:
        ## remove unused rules
        temp_rules = {key: rules[key].copy() for key in rules.keys()}
        rules1 = temp_rules.keys()
        for r1 in list(rules1):
            if r1 in update:
                for ii in range(len(temp_rules[r1])-1, -1, -1):
                    r2 = temp_rules[r1][ii]
                    if r2 not in update:
                        del temp_rules[r1][ii]
                        if len(temp_rules[r1]) == 0:
                            del temp_rules[r1]
            else:
                del temp_rules[r1]
        
        ## reorder update
        corrected_update = []
        for ii in range(len(update)-1, 0, -1):
            for key in temp_rules.keys():
                if len(temp_rules[key]) == ii:
                    corrected_update.append(int(key))
                    if ii == 1:
                        corrected_update.append(temp_rules[key][0])

        ## add middle-point
        solution += corrected_update[len(corrected_update)//2]
    return solution

print(f"Day 5, Part 1 example: {part1(example_file)[0]}")
print(f"Day 5, Part 1 solution: {part1(input_file)[0]}")
 
print(f"Day 5, Part 2 example: {part2(example_file)}")
print(f"Day 5, Part 2 solution: {part2(input_file)}")