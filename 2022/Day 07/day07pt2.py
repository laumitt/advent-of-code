day = '07'
test = 1
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

for pos in range(len(input)):
    if pos > 13:
        lastfour = input[pos-14:pos]
        print(lastfour)
        if len(set(lastfour)) == 14:
            print("ANS", pos)
            break
