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

# print(puzzleinput)

trees = np.zeros((len(puzzleinput[0]), len(puzzleinput[0])))
i=0
for row in puzzleinput:
    j=0
    for a in row:
        trees[i][j] = a
        j+=1
    i+=1

# print(trees)
# print(trees.shape)

scores = []
for y in range(0, trees.shape[0]):
    for x in range(0, trees.shape[0]):
        current = trees[y, x]
        above = np.flip(trees[:y, x])
        # print(above)
        below = trees[y+1:, x]
        # print(below)
        left = np.flip(trees[y, :x])
        # print(left)
        right = trees[y, x+1:]
        # print(right)
        avis = 0
        bvis = 0
        lvis = 0
        rvis = 0
        # print(current)
        for a in above:
            # print("a", a)
            if a < current:
                # print("a+1")
                avis += 1
            else:
                avis += 1
                break
        for b in below:
            # print("b", b)
            if b < current:
                # print("b+1")
                bvis += 1
            else:
                bvis += 1
                break
        for l in left:
            # print("l", l)
            if l < current:
                # print("l+1")
                lvis += 1
            else:
                lvis += 1
                break
        for r in right:
            # print("r", r)
            if r < current:
                # print("r+1")
                rvis += 1
            else:
                rvis += 1
                break
        # print(avis, bvis, lvis, rvis)
        # print("score", avis*bvis*lvis*rvis)
        scores.append(avis * bvis * lvis * rvis)

print(scores)
print(max(scores))
