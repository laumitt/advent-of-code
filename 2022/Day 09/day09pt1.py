import numpy as np

day = '09'
test = 1
if test == 1:
    with open('Day ' + day + '/day'+ day + 'input_test.txt') as f:
        lines = f.readlines()
elif test == 2:
    with open('Day ' + day + '/day'+ day + 'input_test2.txt') as f:
        lines = f.readlines()
else:
    with open('Day ' + day + '/day'+ day + 'input.txt') as f:
        lines = f.readlines()
input = []
for a in range(len(lines)):
    input.append(lines[a].strip())
print(input)

currentH = [0,0]
currentT = [0,0]
tail_visited = set(["[0,0]"])

map = np.zeros([6,6])
map[currentH[0]][currentH[1]] = 1
map[currentT[0]][currentT[1]] = 9
print(np.flipud(map))

for line in input:
    split = line.split(" ")
    dir = split[0]
    steps = int(split[1])
    for i in range(steps):
        if dir == "R":
            newH = [currentH[0], currentH[1]+1]
        elif dir == "L":
            newH = [currentH[0], currentH[1]-1]
        elif dir == "U":
            newH = [currentH[0]+1, currentH[1]]
        elif dir == "D":
            newH = [currentH[0]-1, currentH[1]]
        # print("head", newH)
        currentH = newH

        newT = currentT
        if abs(newH[0] - currentT[0]) > 1:
            if dir == "R":
                newT = [currentT[0], currentT[1]+1]
            elif dir == "L":
                newT = [currentT[0], currentT[1]-1]
            elif dir == "U":
                newT = [currentT[0]+1, currentT[1]]
            else:
                newT = [currentT[0]-1, currentT[1]]
            tail_visited.add(str(newT))
        elif abs(newH[1] - currentT[1]) > 1:
            if dir == "R":
                newT = [currentT[0], currentT[1]+1]
            elif dir == "L":
                newT = [currentT[0], currentT[1]-1]
            elif dir == "U":
                newT = [currentT[0]+1, currentT[1]]
            else:
                newT = [currentT[0]-1, currentT[1]]
            tail_visited.add(str(newT))
        elif abs(newH[0] - currentT[0]) == 1:
            if abs(newH[1] - currentT[1]) == 1:
                # if newH[0] - currentT[0] == 1:
                #     newT[0] = currentT[0]+1
                # elif newH[0] - currentT[0] == -1:
                #     newT[0] = currentT[0]-1
                # elif newH[1] - currentT[1] == 1:
                #     newT[1] = currentT[1]+1
                # elif newH[1] - currentT[1] == -1:
                #     newT[1] = currentT[1]-1
                if dir == "R":
                    newT = [currentT[0]+1, currentT[1]]
                elif dir == "L":
                    newT = [currentT[0]-1, currentT[1]]
                elif dir == "U":
                    newT = [currentT[0], currentT[1]+1]
                elif dir == "D":
                    newT = [currentT[0], currentT[1]-1]

                tail_visited.add(str(newT))

        # print("tail", newT)
        currentT = newT
        lastdir = dir

        print("------------------")
        map = np.zeros([6,6])
        map[newH[0]][newH[1]] = 1
        map[newT[0]][newT[1]] = 9
        print(np.flipud(map))

# print(tail_visited)
print(len(tail_visited))