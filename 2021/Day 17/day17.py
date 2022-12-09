import copy
# import numpy as np
import math
# import matplotlib
day = '17'
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

input = [i for i in lines[0].split(' ')]
xlims = [i for i in input[2][2:-1].split('.')]
ylims = [i for i in input[3][2:].split('.')]
x1 = int(xlims[0])
x2 = int(xlims[2])
y1 = int(ylims[0])
y2 = int(ylims[2])

# print(x1, x2)
# print(y1, y2)

velmax = 10
stepmax = 10
posmax = max(x2, y2)
x_records = []
y_records = []
landings = []
highest = 0

def check_vel_pos(vel, type):
  vel_i = vel
  pos = 0
  max_pos = 0
  results = []
  step = 0
  while pos < posmax and step < stepmax:
    pos += vel
    if pos > max_pos:
      max_pos = pos
    if type == "x":
      if vel > 0:
        vel -= 1
      elif vel < 0:
        vel += 1
      if x1 <= pos <= x2:
        results.append([vel_i, pos, step, max_pos])
        # break
    else:
      vel -= 1
      if y1 <= pos <= y2:
        results.append([vel_i, pos, step, max_pos])
        # break
    step += 1
  return results

# for a in range(0, velmax):
for a in [7, 6, 9]:
  a_ending = check_vel_pos(a,"x")
  if a_ending != []:
    for i in a_ending:
      x_records.append(i)

for b in range(-velmax, velmax):
# for b in [9, 2, 3, 0]:
  b_ending = check_vel_pos(b,"y")
  if b_ending != []:
    for i in b_ending:
      y_records.append(i)

# print("xvel init, xpos fin, step, xmax \n", x_records)
# print("yvel init, ypos fin, step, ymax \n", y_records)

for a in range(0, len(x_records)):
  x = x_records[a]
  for b in range(0, len(y_records)):
    y = y_records[b]
    state = []
    # print("x", x)
    # print("y", y)
    xvel = x[0]
    yvel = y[0]
    xfin = x[1]
    yfin = y[1]
    xste = x[2]
    yste = y[2]
    ymax = y[3]
    print("testing", xvel, yvel)
    state = [xvel, yvel, xfin, yfin, ymax]
    if xste == yste:
      landings.append(state)
      if ymax > highest:
        highest = ymax
      print("lands", state)
print("landings", landings)
print("highest", highest)
print(range(-velmax, velmax))