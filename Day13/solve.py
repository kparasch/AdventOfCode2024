example_file = 'example.txt'
input_file = 'input.txt'

def read_file(input_file: str) -> list[list]:
    infile = open(input_file, 'r')


    A_buttons = []
    B_buttons = []
    prizes = []
    ii = 0
    for line in infile:
        sline = line.strip()
        if ii in [0,1]:
            sline = sline.split(':')[1]
            xx, yy = sline.split(',')
            xx = xx.split('+')[-1]
            yy = yy.split('+')[-1]
            if ii == 0:
                A_buttons.append((int(xx),int(yy)))
            else:
                B_buttons.append((int(xx),int(yy)))
        elif ii == 2:
            sline = sline.split(':')[1]
            xx, yy = sline.split(',')
            xx = xx.split('=')[-1]
            yy = yy.split('=')[-1]
            prizes.append((int(xx), int(yy)))
        ii = (ii+1)%4


    return A_buttons, B_buttons, prizes


def part1(input_file: str) -> int:
    A_buttons, B_buttons, prizes = read_file(input_file)

    solution = 0
    for aa, bb, prize in zip(A_buttons, B_buttons, prizes):
        min_score = -1
        ax, ay = aa
        bx, by = bb
        px, py = prize
        max_na = int(px / ax) + 1
        for na in range(max_na):
            res = px - na*ax
            if res%bx == 0:
                nb = res // bx
                if na*ay + nb*by == py:
                    score = 3*na + 1*nb
                    if min_score < 0 or score < min_score:
                        min_score = score

        if min_score > 0:
            solution += min_score


    return solution 


def part2(input_file: str) -> int:
    A_buttons, B_buttons, prizes = read_file(input_file)


    A_buttons, B_buttons, prizes = read_file(input_file)

    solution = 0
    for aa, bb, prize in zip(A_buttons, B_buttons, prizes):
        min_score = -1
        ax, ay = aa
        bx, by = bb
        px, py = prize
        px += 10000000000000
        py += 10000000000000
        det = (ax*by - bx*ay)
        nad = (by*px-bx*py)
        nbd = (-ay*px+ax*py)
        na = nad//det
        nb = nbd//det
        min_score =  3*na + nb

        if nad % det == 0 and nbd % det == 0:
            solution += min_score


    return solution 


print(f"Day 13, Part 1 example: {part1(example_file)}")
print(f"Day 13, Part 1 solution: {part1(input_file)}")

print(f"Day 13, Part 2 example: {part2(example_file)}")
print(f"Day 13, Part 2 solution: {part2(input_file)}")