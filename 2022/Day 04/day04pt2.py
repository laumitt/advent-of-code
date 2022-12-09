day = '04'
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

fully = 0
numover = 0
for i in input:
    [elf1, elf2] = i.split(",")
    assigns = [elf1, elf2]
    sections1 = [x for x in range(int(elf1.split('-')[0]), int(elf1.split('-')[1])+1)]
    sections2 = [y for y in range(int(elf2.split('-')[0]), int(elf2.split('-')[1])+1)]
    # print("sections1", sections1)
    # print("sections2", sections2)
    overlap = set(sections1).intersection(set(sections2))
    print("overlap", overlap)
    if len(overlap) > 0:
        numover += 1
    if overlap == set(sections1):
        fully += 1
        # print("plus1", sections1, "|", overlap)
    elif overlap == set(sections2):
        fully += 1
        # print("plus1", sections2, "|", overlap)

print(fully)
print('sections overlapped', numover)
