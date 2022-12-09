day = '03'
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

caps = {}
for i in range(65,91):
    caps[chr(i)] = i-38
print(caps)

lower = {}
for i in range(97, 123):
    lower[chr(i)] = i-96
print(lower)

total = 0

numsets = len(input)/3
print(numsets)

for i in range(0, len(input), 3):
    score = 0
    pt1 = input[i]
    pt2 = input[i+1]
    pt3 = input[i+2]
    for i in set(pt1):
        if i in set(pt2):
            if i in set(pt3):
                print(i)
                if i in caps:
                    score = caps[i]
                    print(caps[i])
                elif i in lower:
                    score = lower[i]
                    print(lower[i])
                else:
                    print('ahh')
    total += score

print(total)
