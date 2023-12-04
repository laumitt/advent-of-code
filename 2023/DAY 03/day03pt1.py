day = '03'
test = 1
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

import numpy as np

# arr = np.array(input).reshape(len(input), 1)
# print(arr)

for i in input:
    print("i", i)
    for j in i:
        # print(k)
        if not j.isdigit() and not j==".":
            print("special", j)
            print("overall", input.index(i), i.index(j))
            around_specials = [[input.index(i)-1, i.index(j)-1],
                               [input.index(i)-1, i.index(j)],
                               [input.index(i)-1, i.index(j)+1],
                               [input.index(i), i.index(j)-1],
                               [input.index(i), i.index(j)+1],
                               [input.index(i)+1, i.index(j)-1],
                               [input.index(i)+1, i.index(j)],
                               [input.index(i)+1, i.index(j)+1]]
            print(around_specials)
            for char in around_specials:
                if input[char[0]][char[1]].isdigit():
                    print(char,input[char[0]][char[1]])