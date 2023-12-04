day = '03'
test = 0
if test == 1:
    with open('DAY 03\day03input_test.txt') as f:
        lines = f.readlines()
else:
    with open('DAY 03\day03input.txt') as f:
        lines = f.readlines()
input = []
for a in range(len(lines)):
    input.append(lines[a].strip())
print(input)
