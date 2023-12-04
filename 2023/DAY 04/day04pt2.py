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
matches = {}
copies = {}
for card in input:
    print(((card.split(':')[0]).strip()).split()[1])
    cardnum = int(((card.split(':')[0]).strip()).split()[1])
    matches[cardnum] = 0
    copies[cardnum] = 1
    winning, have = ((card.split(':')[1]).strip()).split(' | ')
    for num in winning.split(" "):
        if num in have.split(" ") and num.isdigit():
            matches[cardnum] += 1
print("matches", matches)

for cardnum in matches:
    for i in range(matches[cardnum]+1):
        if i > 0:
            copies[cardnum+i] += 1*copies[cardnum]
print(copies)

total = 0
for cardnum in copies:
    total += copies[cardnum]
print('total', total)