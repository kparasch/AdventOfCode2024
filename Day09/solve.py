from collections import deque

example_file = 'example.txt'
input_file = 'input.txt'



def read_file(input_file: str) -> list[int]:
    infile = open(input_file, 'r')

    for line in infile:
        diskmap = deque(map(int,line.strip()))
        break

    return diskmap



def part1(input_file: str) -> int:
    diskmap = read_file(input_file) 


    left_id = 0
    right_id = len(diskmap)//2
    left_pos = -1
    checksum = 0
    right_size = diskmap.pop()
    while len(diskmap):
        blocksize = diskmap.popleft()
        for _ in range(blocksize):
            left_pos += 1
            checksum += left_pos * left_id
        left_id += 1

        emptyspace = diskmap.popleft()
        for _ in range(emptyspace):
            if right_size == 0:
                diskmap.pop()
                right_size = diskmap.pop()
                assert right_size > 0
                right_id -= 1
            left_pos += 1
            checksum += left_pos*right_id
            right_size -= 1

    for _ in range(right_size):
        left_pos += 1
        checksum += left_pos*right_id

    return checksum 
            


def part2(input_file: str) -> int:
    diskmap = read_file(input_file) 

    # get starting position if not moved
    starting_pos = []
    right_id = len(diskmap)//2
    left_pos = 0
    for ii in range(right_id):
        starting_pos.append(left_pos)
        left_pos += diskmap[2*ii] + diskmap[2*ii+1]
    starting_pos.append(left_pos)
        
    emptyspaces = []
    left_pos = 0
    for ii in range(right_id):
        left_pos += diskmap[2*ii]
        empty_size = diskmap[2*ii+1]
        if empty_size > 0:
            emptyspaces.append((empty_size, left_pos))
        left_pos += empty_size

    frags = []
    
    for ii in range(right_id, -1, -1):
        moved = False
        frag_size = diskmap[2*ii]
        frag_pos = starting_pos[ii]
        for jj in range(len(emptyspaces)):
            empty_size, empty_pos = emptyspaces[jj]
            if empty_pos > frag_pos:
                break
            if empty_size >= frag_size:
                moved = True
                frag_pos = empty_pos
                empty_size -= frag_size
                empty_pos += frag_size
                frags.append((ii, frag_size, frag_pos))
                if empty_size > 0:
                    emptyspaces[jj] = (empty_size, empty_pos)
                else:
                    del emptyspaces[jj]
                break
        if not moved:
            frags.append((ii, frag_size, frag_pos))
            

    checksum = 0
    for frag_id, frag_size, frag_pos in frags:
        for ii in range(frag_size):
            checksum += frag_id*frag_pos
            frag_pos += 1

    return checksum

print(f"Day 9, Part 1 example: {part1(example_file)}")
print(f"Day 9, Part 1 solution: {part1(input_file)}")
  
print(f"Day 9, Part 2 example: {part2(example_file)}")
print(f"Day 9, Part 2 solution: {part2(input_file)}")