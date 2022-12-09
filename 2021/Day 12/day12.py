import copy
test = 1
if test == 1:
    with open('day12input_test.txt') as f:
        lines = f.readlines()
elif test == 2:
    with open('day12input_test2.txt') as f:
        lines = f.readlines()
else:
    with open('day12input.txt') as f:
        lines = f.readlines()
input = []
for a in range(len(lines)):
    input.append(lines[a].strip().split("-"))

class big_cave:
    visit_again = True
    connections = []

class small_cave:
    visit_again = False
    connections = []

caves = {}

for b in input:
    for c in b:
        if c not in caves:
            if c.isupper():
                d = big_cave()
                caves[c] = copy.deepcopy(d)
            else:
                e = small_cave()
                caves[c] = copy.deepcopy(e)

for f in caves:
    for g in input:
        if g[0] == f:
            print("g0", g[0])
            caves[f].connections.append(g[1])
            print("f", f)
            print("g[1]", g[1])
            print(f, "conn to", caves[f].connections)
            # print("b1 conn", caves[b[1]].connections)

for i in caves:
    print(i, "conn", caves[i].connections)
