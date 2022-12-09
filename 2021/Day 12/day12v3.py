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
    visited = False
    connections = []

class small_cave:
    visit_again = False
    visited = False
    connections = []

def define_caves():
    caves = {}
    for b in input:
        for c in b:
            if c not in caves:
                # print("cave", c)
                if c == "start":
                    d = small_cave()
                elif c == "end":
                    d = small_cave()
                elif c.isupper():
                    d = big_cave()
                else:
                    d = small_cave()
                caves[c] = copy.deepcopy(d)
    return caves

def find_conns(current_place):
    # print("current place", current_place)
    new_conns = []
    for line in input:
        # print("line 0", line[0])
        # print('line 1', line[1])
        if line[0] == current_place:
            new_conns.append(line[1])
        elif line[1] == current_place:
            new_conns.append(line[0])
        # print("new conns", new_conns)
    return new_conns

def compile_conns(cave_list):
    all_conns = {}
    for c in cave_list:
        conns = cave_list[c].connections
        print("conns", conns)
        for e in conns:
            print("connection", e)
            next_conns = cave_list[e].connections
            print("next conns", next_conns)
            all_conns[e] = next_conns
    print("all conns", all_conns)
    return all_conns

def next_step(current, cave_list, all_conns):
    path = []
    print("current", current)
    print("connections", all_conns[current])
    for i in all_conns[current]:
        next = i
        if next == "end":
            path.append(next)
            break
        else:
            path.append(next)
    return path

def main():
    all_paths = []
    cave_list = define_caves()
    for cave in cave_list:
        cave_list[cave].connections = find_conns(cave)
        # print("cave and conns", cave, cave_list[cave].connections)
    # print("cave list", cave_list)
    print("---- compile conns ----")
    all_conns = compile_conns(cave_list)
    print("---- next step ----")
    for cave in cave_list:
        all_paths.append(next_step(cave, cave_list, all_conns))
    print(all_paths)

if __name__ == '__main__':
    main()
