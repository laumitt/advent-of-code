day = '02'
test = 0
if test == 1:
    with open('DAY 02\day02input_test.txt') as f:
        lines = f.readlines()
else:
    with open('DAY 02\day02input.txt') as f:
        lines = f.readlines()
input = []
for a in range(len(lines)):
    input.append(lines[a].strip())
print(input)

cubecolors = ['red', 'green', 'blue']
cubedata = {}
for game in input:
    gamenum = int((game.split(':')[0]).split(' ')[-1])
    cubesets = (game.split(':')[1]).split(';')
    # print('cubesets', cubesets)
    # print('len', len(cubesets))
    cubedata[gamenum] = {}
    for i in range(len(input)):
        for j in range(len(cubesets)):
            cubedata[gamenum][j] = {"red":0, "green":0, "blue":0}
            record = cubesets[j]
            # print('record', record)
            each = record.split(',')
            # print('each', each)
            for e in each:
                for color in cubecolors:
                    if color in e:
                        cubedata[gamenum][j][color] = int(e.split(' ')[1])
# print(cubedata)

total = 0
for game in cubedata:
    print(game)
    print(cubedata[game])
    minred = 0
    mingreen = 0
    minblue = 0
    for set in cubedata[game]:
        minred = max(minred, cubedata[game][set]['red'])
        mingreen = max(mingreen, cubedata[game][set]['green'])
        minblue = max(minblue, cubedata[game][set]['blue'])
    power = minred * mingreen * minblue
    print('power', power)
    total += power
print('total', total)