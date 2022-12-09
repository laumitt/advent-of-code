import numpy as np

day = '08'
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

for y in range(1, trees.shape[0]-1):
    for x in range(1, trees.shape[0]-1):
        current = trees[y, x]
        above = trees[:y, x]
        below = trees[y+1:, x]
        left = trees[y, :x]
        right = trees[y, x+1:]
        if max(above) < current or max(below) < current or max(left) < current or max(right) < current:
            visible += 1

print(visible)
