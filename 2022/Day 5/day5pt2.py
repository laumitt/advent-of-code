import re

day = '5'
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

boxes = lines[:lines.index("\n")]
instructions = lines[lines.index("\n")+1:]

boxinput = []
for a in range(len(boxes)):
    boxinput.append(boxes[a].strip("\n"))
    
instrinput = []
for a in range(len(instructions)):
    instrinput.append(instructions[a].strip("\n"))

print(boxinput)
print(instrinput)

cols = int(boxinput[-1][-2])
print(cols)

stacks = {}
for c in range(cols):
    stacks[c+1] = []

for box in boxinput[:-1]:
    print(box)
    for char in range(0, len(box)+1, 4):
        if box[char:char+3] != '   ':
            stacks[char/4 + 1].append(box[char:char+3])

print(stacks)
for c in stacks:
    print(c, "has boxes", len(stacks[c]))

print(instrinput)

for line in instrinput:
    n = re.search("move ", line)
    f = re.search(" from ", line)
    t = re.search(" to ", line)
    print(line[t.span()[1]:])
    numtomove = int(line[n.span()[1]:f.span()[0]])
    fromcol = int(line[f.span()[1]:t.span()[0]])
    tocol = int(line[t.span()[1]:])
    print(line, "\n", numtomove, fromcol, tocol)
    # print(stacks)
    stacks[tocol] = stacks[fromcol][0:numtomove] + stacks[tocol]
    del stacks[fromcol][0:numtomove]
    for c in stacks:
        print(c, "has boxes", len(stacks[c]))
print(stacks)


topcols = ""
for column in stacks:
    try:
        topcols += stacks[column][0].strip("[").strip("]")
    except IndexError:
        continue

print(topcols)