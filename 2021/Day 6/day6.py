import copy
import numpy as np
day = '6'
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
input = [int(i) for i in lines[0].split(',')]

fish = input
# print(fish)

# part 1
# num_days = 80
# for i in range(num_days):
#   updated = [copy.deepcopy(0)]*len(fish)
#   new_count = 0
#   for a, ele in enumerate(fish):
#     # print(fish[a])
#     if fish[a] == 0:
#       updated[a] = 6
#       updated.append(8)
#     else:
#       updated[a] = fish[a]-1
#   fish = updated
#   # print(fish)
# num_fish = len(fish)

# part 2 shamelessly copied from nabih/amit bc the above timed out too much
num_days = 256
today = [0,0,0,0,0,0,0,0,0]
for i in fish:
  today[i] += 1

for i in range(num_days):
  new_fish = today[0] # track number of new fish to make
  today[0:8] = today[1:] # move everything over one (count down by 1)
  today[8] = new_fish # add number of new fish created (9 day countdown)
  today[6] += new_fish # add to 7 day countdown
num_fish = sum(today)

print(num_fish)





