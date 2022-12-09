day = '6'
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
input = list(input[0])

print(input)

for pos in range(len(input)):
    if pos > 3:
        lastfour = input[pos-4:pos]
        print(lastfour)
        if len(set(lastfour)) == 4:
            print("ANS", pos)
            break
