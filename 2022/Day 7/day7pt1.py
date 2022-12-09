day = '7'
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

sizes = {'/' : 0}
conts = {'/' : []}

for logline in input:
    line = logline.split(" ")
    print(line)
    if line[0] == "dir":
        sizes[line[1]] = 0
        conts[curdir].append(line[1])
    elif line[1] == "cd":
        curdir = line[2]
    elif line[0] != "$":
        sizes[curdir] += int(line[0])
    
    # if line[0] == "$":
    #     if line[1] == "cd":
    #         dir = line[2]
    # else:
    #     sizes[dir] += int(line[0])

print(sizes)