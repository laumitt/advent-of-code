import copy
day = '21'
test = 0
if test == 1:
    with open('day'+ day + 'input_test.txt') as f:
        lines = f.readlines()
elif test == 2:
    with open('day'+ day + 'input_test2.txt') as f:
        lines = f.readlines()
else:
    with open('day'+ day + 'input.txt') as f:
        lines = f.readlines()

# part 1 rules
# deterministic die counts 1 to 100 on loop
# random starting space for p1 and p2
# roll die 3 times then add results
# move total number of spaces around track
# add space number to player score
# first to hit 1000 or more wins instantly
# puzzle answer is num rolls * losing score

p1_start = lines[0][28:].strip()
p2_start = lines[1][28:].strip()

die_shows = 1
p1_place = int(p1_start)
p2_place = int(p2_start)
p1_score = 0
p2_score = 0
turn = "p1"
num_rolls = 0
game_won = False

print("turn", turn)
print("p1 status", [p1_place, p1_score])
print("p2 status", [p2_place, p2_score])

while game_won == False:
  turn_roll = 0
  for i in range(3):
    turn_roll += die_shows
    die_shows = die_shows % 100
    die_shows += 1
    num_rolls += 1
  if turn == "p1":
    p1_place += turn_roll
    p1_place = (p1_place-1) % 10
    p1_place += 1
    p1_score += p1_place
  elif turn == "p2":
    p2_place += turn_roll
    p2_place = (p2_place-1) % 10
    p2_place += 1
    p2_score += p2_place
  print("rolled", turn_roll)
  print("turn", turn)
  print("p1 status", [p1_place, p1_score])
  print("p2 status", [p2_place, p2_score])
  
  if p1_score >= 1000 or p2_score >= 1000:
    game_won = True
    print('game over')
  if turn == "p1":
    turn = "p2"
  elif turn == "p2":
    turn = "p1"
  else:
    print('oops 2')

print("p1 score", p1_score)
print("p2 score", p2_score)
print("number of rolls", num_rolls)

if p1_score > p2_score:
  print("p1 wins with score", p1_score)
  ans = p2_score * num_rolls
  print("puzzle answer", ans)
elif p2_score > p1_score:
  print("p2 wins with score", p2_score)
  ans = p1_score * num_rolls
  print("puzzle answer", ans)