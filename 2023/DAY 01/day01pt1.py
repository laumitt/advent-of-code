day = '01'
test = 0
if test == 1:
    with open('DAY 01\day01input_test.txt') as f:
        lines = f.readlines()
else:
    with open('DAY 01\day01input.txt') as f:
        lines = f.readlines()
input = []
for a in range(len(lines)):
    input.append(lines[a].strip())
print(input)

numbers = []
for calnum in input:
    # print(calnum)
    digits_this_line = []
    for letter in calnum:
        # print(letter)
        if letter.isnumeric():
            digits_this_line.append(letter)
    numbers.append(digits_this_line[0]+digits_this_line[-1])

total = 0
for num in numbers:
    print(num)
    total += int(num)

print(total)