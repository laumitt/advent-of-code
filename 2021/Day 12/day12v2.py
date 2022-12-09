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

def find_conns(current_place):
    new_conns = []
    for line in input:
        print(line)
        if line[0] == current_place:
            new_conns += line[1]
        elif line[1] == current_place:
            new_conns += line[0]
    return new_conns

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
all_conns = []
current_place = caves["start"]
paths = find_conns(current_place)
print("paths", paths)
for i in paths:
    current_place = i
    conns = find_conns(current_place)
    print("conns")
    for j in conns:
        print('j loop')
        current_place.connections.append([i,j])
        all_conns.append([i, j])
        print(current_place.connections)
print(all_conns)
