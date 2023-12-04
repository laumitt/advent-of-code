day = '04'
test = 0
if test == 1:
    with open('DAY 04\day04input_test.txt') as f:
        lines = f.readlines()
else:
    with open('DAY 04\day04input.txt') as f:
        lines = f.readlines()
input = []
for a in range(len(lines)):
    input.append(lines[a].strip())
print(input)

total = 0
points = []
for card in input:
    doubletimes = 0
    winning, have = ((card.split(':')[1]).strip()).split(' | ')
    for num in winning.split(" "):
        if num in have.split(" ") and num.isdigit():
            doubletimes += 1
    if doubletimes != 0:
        points.append(2**(doubletimes-1))
    else:
        points.append(0)

print("points", points)
total = sum(points)
print("total", total)