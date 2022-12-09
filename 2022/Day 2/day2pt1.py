day = '2'
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
             "X" : "R",
             "Y" : "P",
             "Z" : "S"}

hierarchy = {"R": {"R" : "D", "P" : "L", "S" : "W"},
             "P": {"R" : "W", "P" : "D", "S" : "L"},
             "S": {"R" : "L", "P" : "W", "S" : "D"}}

scores = {"W": 6, "D": 3, "L" : 0,
          "R": 1, "P": 2, "S": 3}

totalscore = 0

for round in input:
    opp = mapping[round[0]]
    you = mapping[round[-1]]
    print(opp, you)
    result = hierarchy[you][opp]
    roundscore = scores[result]+scores[you]
    print(result, roundscore)
    totalscore += roundscore

print("total", totalscore)
