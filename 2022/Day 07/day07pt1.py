day = '07'
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

# print(input)

curdir = []
files = {}

# referencing florian's code because i got stuck
for logline in input:
    line = logline.split(" ")
    print(line)
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] != "..":
                curdir.append(line[2])
            else:
                curdir.remove(curdir[-1])
    else:
        if line[0].isdigit():
            places = int(line[0])
        else:
            places = "/" + curdir + "/" + line[1]
        if "/" + curdir in files:
            files["/" + curdir].append(places)
        else:
            files["/" + curdir] = places

# total = 0
# for file in files:
#     size += 


# print(sizes)