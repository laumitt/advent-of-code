import copy
import numpy
day = '4'
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
input = []
for a in range(len(lines)):
    input.append(lines[a].strip())

# first line is numbers being called
# each board is 5 by 5, each number is 2 characters
# boards separated by empty line, numbers separated by space
# mark board as numbers are called
# win with at least one complete row or column
# winning board score is sum of unmarked numbers times last number called

def check_win(markings):
  board_wins = False
  row_scores = {}
  col_scores = {}
  for i in range(len(markings)):
    row_scores[i] = 0
  for j in range(len(markings[0])):
    col_scores[j] = 0
  for x in range(len(markings)):
    for y in range(len(markings[x])):
      row_scores[x] += markings[x][y]
      col_scores[y] += markings[x][y]
  for a in row_scores:
    if row_scores[a] == 5:
      board_wins = True
  for b in col_scores:
    if col_scores[b] == 5:
      board_wins = True
  return board_wins

def score_board(board, markings, last_call):
  unmarked = 0
  for a in range(len(markings)):
    for b in range(len(markings[a])):
      if markings[a][b] == 0:
        unmarked += board[a][b]
  score = unmarked*last_call
  return score

calls = [int(i) for i in input[0].split(",") if i.isdigit()]
all_boards = input[1:]
num_boards = int(len(all_boards)/6)
boards = {}
markings = {}
offset = 1

for a in range(num_boards):
  this_board = []
  ab_index = a*5 + offset
  for b in range(5):
    split_row = [int(i) for i in all_boards[ab_index + b].split(" ") if i.isdigit()]
    this_board.append(split_row)
  offset += 1
  # print(this_board)
  boards[a] = this_board
  markings[a] = numpy.zeros_like(this_board)

# print(boards)
# print(markings)

# part 1 - find score of first board to win
# for e in calls:
#   # print("called", e)
#   for f in range(num_boards):
#     board = boards[f]
#     marks = markings[f]
#     for line in board:
#       for num in line:
#         if num == e:
#           line_place = line.index(num)
#           board_place = board.index(line)
#           marks[board_place][line_place] = 1
#     is_winner = check_win(marks)
#     if is_winner:
#       winner = board
#       score = score_board(board, marks, e)
#       print("board", f, "wins with score", score)
  #     break
  # if is_winner:
  #   break

# part 2 - find score of last board to win
boards_left = copy.deepcopy(boards)
keys_left = list(boards_left.keys())
for e in calls:
  # print("called", e)
  for f in keys_left:
    board = boards_left[f]
    marks = markings[f]
    for line in board:
      for num in line:
        if num == e:
          line_place = line.index(num)
          board_place = board.index(line)
          marks[board_place][line_place] = 1
    is_winner = check_win(marks)
    if is_winner:
      del boards_left[f]
    keys_left = list(boards_left.keys())
    if len(keys_left) == 0:
      score = score_board(board, marks, e)
      print("last board wins with score", score)