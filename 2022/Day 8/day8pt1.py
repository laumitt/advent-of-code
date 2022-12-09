import numpy as np

day = '8'
test = 0
if test == 1:
    with open('Day ' + day + '/day'+ day + 'input_test.txt') as f:
        lines = f.readlines()
elif test == 2:
    with open('Day ' + day + '/day'+ day + 'input_test2.txt') as f:
        lines = f.readlines()
else:
    with open('Day ' + day + '/day'+ day + 'input.txt') as f:
        lines = f.readlines()
puzzleinput = []
for a in range(len(lines)):
    puzzleinput.append(lines[a].strip())

print(puzzleinput)

trees = np.zeros((len(puzzleinput[0]), len(puzzleinput[0])))
i=0
for row in puzzleinput:
    j=0
    for a in row:
        trees[i][j] = a
        j+=1
    i+=1

print(trees)
print(trees.shape)

visible = trees.shape[0]*4-4
print(visible)

insidedim = trees.shape[0]-2
for i in range(insidedim):
    y = i+1
    for j in range(insidedim):
        x = j+1
        current = trees[y, x]
        # print("coordinates", x, y)
        above = trees[:x, y]
        below = trees[x+1:, y]
        left = trees[x, :y]
        right = trees[x, y+1:]
        print("a", len(above))
        print("b", len(below))
        print(len(above) + len(below))
        print("l", len(left))
        print("r", len(right))
        print(len(left) + len(right))
        if max(above) < current or max(below) < current or max(left) < current or max(right) < current:
            visible += 1
            print(x, y, current)

print(visible)
