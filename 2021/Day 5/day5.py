import copy
import numpy as np
day = '5'
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

if test == 1:
  size = 10
else:
  size = 1000
map = np.zeros([size,size])

for line in input:
  coords = line.split(" -> ")
  print(coords)
  x1 = int(coords[0].split(",")[0])
  y1 = int(coords[0].split(",")[1])
  x2 = int(coords[1].split(",")[0])
  y2 = int(coords[1].split(",")[1])
  lo_x = min(x1, x2)
  hi_x = max(x1, x2)
  lo_y = min(y1, y2)
  hi_y = max(y1, y2)
  # print(x1, y1, x2, y2)
  x_diff = hi_x - lo_x
  y_diff = hi_y - lo_y
  # part 1 - horizontal or vertical lines
  if x_diff == 0 or y_diff == 0:
    x_points = list(range(lo_x, hi_x+1))
    y_points = list(range(lo_y, hi_y+1))
    for map_y in y_points:
      for map_x in x_points:
        map[map_y][map_x] += 1
    # print("x", x_points)
    # print("y", y_points)
  # part 2 - diagonal lines
  elif x_diff == y_diff:
    pairs = []
    for a in range(x_diff+1):
      if x1 == lo_x:
        if y1 == lo_y:
          pair = [x1+a, y1+a]
        elif y1 == hi_y:
          pair = [x1+a, y1-a]
      elif x1 == hi_x:
        if y1 == lo_y:
          pair = [x1-a, y1+a]
        elif y1 == hi_y:
          pair = [x1-a, y1-a]
      pairs.append(pair)
    for b in pairs:
      map[b[1]][b[0]] += 1

print(map)

count = 0
for row in map:
  for point in row:
    if point >= 2:
      count += 1
print(count)