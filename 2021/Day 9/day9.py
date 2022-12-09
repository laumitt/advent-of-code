import copy
import numpy as np
day = '9'
test = 1
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
# print(input)

mod_hei = len(input)+2
mod_wid = len(input[0])+2
map = np.zeros([mod_hei, mod_wid])
# print(map)
for b in range(mod_hei):
  map[b][0] = 9
  map[b][-1] = 9
for c in range(mod_wid):
  map[0][c] = 9
  map[-1][c] = 9
# print(map)
for d in range(len(input)):
  for e in range(len(input[0])):
    map[d+1][e+1] = input[d][e]
print(map)

# # part 1 - risk scores
# risk_total = 0
# for i in range(len(map)+1):
#   if i == 0 or i >= len(map)-1:
#     continue
#   for j in range(len(map[i])+1):
#     if j == 0 or j >= len(map[i])-1:
#       continue
#     # print(i, j)
#     point = map[i][j]
#     above = map[i-1][j]
#     below = map[i+1][j]
#     left = map[i][j-1]
#     right = map[i][j+1]
#     if point < above and point < below and point < left and point < right:
#       risk_total += point + 1
# print(risk_total)

# part 2 - basins
for i in range(len(map)+1):
  if i == 0 or i >= len(map)-1:
    continue
  for j in range(len(map[i])+1):
    if j == 0 or j >= len(map[i])-1:
      continue
    