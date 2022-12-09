test = 0
if test == 1:
    with open('day11input_test.txt') as f:
        lines = f.readlines()
elif test == 2:
    with open('day11input_test2.txt') as f:
        lines = f.readlines()
else:
    with open('day11input.txt') as f:
        lines = f.readlines()
input = []
for a in range(len(lines)):
    input.append(lines[a].strip())

import copy

# steps of energy
# increase energy by 1
# loop
    # energy greater than 9 flash if they haven't already flashed this step
    # increase energy of neighbors by 1
# anything that flashed this step sets energy to 0
# add to count of number of flashes
# repeat for 100 steps

global num_flashes

def check_flash(flashed, new_octopi, d, e):
    global num_flashes
    if new_octopi[d][e] > 9:
        if flashed[d][e] == False:
            print('flashing', d, e, 'was', new_octopi[d][e])
            flashed[d][e] = True
            new_octopi[d][e] = 0
            num_flashes += 1
            print(num_flashes)
            check_neighbors(flashed, new_octopi, d, e)

def check_neighbors(flashed, new_octopi, d, e):
    for f in range(len(new_octopi)):
        for g in range(len(new_octopi[f])):
            if f == d-1 or f == d or f == d+1:
                if g == e-1 or g == e or g == e+1:
                    if flashed[f][g] == False:
                        new_octopi[f][g] += 1
                        check_flash(flashed, new_octopi, f, g)

new_octopi = [[copy.deepcopy(False) for i in range(len(input[0]))] for j in range(len(input))]
for b in range(len(input)):
    for c in range(len(input[b])):
        new_octopi[b][c] = int(input[b][c])

step_add = [[1]*len(new_octopi[0])]*len(new_octopi)
num_steps = 300
num_flashes = 0
flag = True
x = 0
while True:
    flag = True
    x += 1
    flashed = [[copy.deepcopy(False) for i in range(len(new_octopi[0]))] for j in range(len(new_octopi))]
    for d in range(len(new_octopi)):
        for e in range(len(new_octopi[d])):
            if flashed[d][e] == False:
                new_octopi[d][e] = new_octopi[d][e] + 1
                check_flash(flashed, new_octopi, d, e)
    # print('flashed', flashed)
    # print("new", new_octopi)
    for m in flashed:
        for n in m:
            if n == False:
                flag = False
    if flag:
        print("step", x)
        break
    else:
        print("ek")


# print(num_flashes)
