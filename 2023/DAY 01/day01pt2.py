day = '01'
test = 0
if test == 1:
    with open('DAY 01\day01input_test.txt') as f:
        lines = f.readlines()
elif test == 2:
    with open('DAY 01\day01input_test2.txt') as f:
        lines = f.readlines()
else:
    with open('DAY 01\day01input.txt') as f:
        lines = f.readlines()
input = []
for a in range(len(lines)):
    input.append(lines[a].strip())
print(input)

numberwords = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
               "six": 6, "seven": 7, "eight": 8, "nine": 9,
               "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
numbers = []

def sortfunc(list):
    return list['index']

for calnum in input:
    print(calnum)
    digits_list = []
    for num in numberwords:
        if num in calnum:
            digits_list.append({"digit": numberwords[num], "index": calnum.index(num)})
            digits_list.append({"digit": numberwords[num], "index": calnum.rindex(num)})
            print("num", num)
            print("indexed", calnum[calnum.index(num)])
            print("rindexed", calnum[calnum.rindex(num)])
            print("dict", numberwords[num])
    digits_list.sort(key=sortfunc)
    print(digits_list)
    numbers.append(str(digits_list[0]['digit'])+str(digits_list[-1]['digit']))

total = 0
for num in numbers:
    print(num)
    total += int(num)

print(total)
