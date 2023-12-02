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

maxred = 12
maxgreen = 13
maxblue = 14
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
    possiblesets = 0
    # print(cubedata[game])
    # print(maxred, maxgreen, maxblue)
    for set in cubedata[game]:
        # print('set', cubedata[game][set])
        if cubedata[game][set]['red'] <= maxred and cubedata[game][set]['green'] <= maxgreen and cubedata[game][set]['blue'] <= maxblue:
            possiblesets += 1
            # print('set possible')
    # print(len(cubedata[game]))
    # print(possiblesets)
    if possiblesets == len(cubedata[game]):
        # print('game possible')
        total += game
print('total', total)