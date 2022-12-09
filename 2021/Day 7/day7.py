import copy
import numpy as np
day = '7'
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
input = [int(i) for i in lines[0].split(',')]

# print(input)

min_fuel = 0
min_pos = 0
for a in range(min(input), max(input)+1):
  fuel = 0
  for b in input:
    dist = abs(b-a)
    fuel += (dist*(dist+1))/2
  if min_fuel == 0 or fuel < min_fuel:
    min_pos = a
    min_fuel = fuel
print(min_fuel, "to", min_pos)