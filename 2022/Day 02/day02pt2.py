day = '02'
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

# rock beats scissors beats paper beats rock
# rock = a, x, 1
# paper = b, y, 2
# scissors = x, z, 3
# loss = 0, draw = 3, win = 6

mapping = {"A" : "R",
             "B" : "P",
             "C" : "S",
             "X" : "L",
             "Y" : "D",
             "Z" : "W"}

hierarchy = {"R": {"D" : "R", "W" : "P", "L" : "S"},
             "P": {"L" : "R", "D" : "P", "W" : "S"},
             "S": {"W" : "R", "L" : "P", "D" : "S"}}

scores = {"W": 6, "D": 3, "L" : 0,
          "R": 1, "P": 2, "S": 3}


totalscore = 0

for round in input:
    opp = mapping[round[0]]
    res = mapping[round[-1]]
    print(opp, res)
    you = hierarchy[opp][res]
    roundscore = scores[you]+scores[res]
    print(opp, res, you, scores[you], scores[res], roundscore)
    totalscore += roundscore

print("total", totalscore)
