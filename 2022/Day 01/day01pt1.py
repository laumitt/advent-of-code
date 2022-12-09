import copy
day = '01'
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
input = []
for a in range(len(lines)):
    input.append(lines[a].strip())

print(input)
elves = []
cal = 0

for i in input:
    print(str(i))
    if i != "":
        cal += int(i)
    else:
        elves.append(cal)
        cal = 0
print("max", max(elves))

total = 0
elves.sort()
for cals in elves[-3:]:
    print(cals)
    total += cals

print("total", total)
