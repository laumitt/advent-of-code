test = 1
if test == 1:
    with open('day3input_test.txt') as f:
        lines = f.readlines()
else:
    with open('day3input.txt') as f:
        lines = f.readlines()
input = []
for a in range(len(lines)):
    input.append(lines[a].strip())

# oxygen - most common, keep 1
# co2 - least common, keep 0

for b in range(len(input)):
    for c in range(len(input[b])):
        print(c) # don't actually do this
