# this boi broken

with open('day8input_test.txt') as f:
    lines = f.readlines()

input = []
for a in range(len(lines)):
    input.append(lines[a])

outputs = []
for b in range(len(input)):
    parts = input[b].strip().split(" | ")
    outputs.append(parts[1])

digit = ""
total = 0
digits = []

for c in range(len(outputs)):
    display = outputs[c].split(" ")
    known = False
    digit = ""
    part = ""
    over_one = 0
    over_two = 0
    over_thre = 0
    over_four = 0
    over_five = 0
    while known == False:
        for d in range(len(display)):
            curr = display[d]
            one = ""
            two = ""
            three = ""
            four = ""
            five = ""
            if len(curr) == 2:
                part = "1"
                one = curr
            elif len(curr) == 3:
                part = "7"
            elif len(curr) == 4:
                part ="4"
                four = curr
            elif len(curr) == 7:
                part ="8"
            elif len(curr) == 5:
                # part = "2, 3, 5"
                for e in range(len(curr)):
                    if curr[e] in one:
                        over_one = over_one + 1
                    if curr[e] in four:
                        over_four = over_four + 1
                if over_one == 2:
                    part ="3"
                    three = curr
                elif over_four == 3:
                    part ="5"
                    five = curr
                elif over_four == 2:
                    part ="2"
                    two = curr
            elif len(curr) == 6:
                # part = "0, 6, 9"
                for g in range(len(curr)):
                    if curr[g] in one:
                        over_one = over_one + 1
                    if curr[g] in five:
                        over_five = over_five + 1
                    if curr[g] in four:
                        over_four = over_four + 1
                if over_four == 4:
                    part ="9"
                elif over_five == 5:
                    part ="6"
                elif over_one == 2:
                    part ="0"
            if part != "":
                print("part", part)
                digit += part
            if len(digit) == 4:
                print("digit", digit)
                digits.append(digit)
                known = True
for i in range(len(digits)):
    total += int(digit)
print("total", total)
