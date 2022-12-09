import copy
# import numpy as np
import math
from collections import Counter
day = '14'
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
currentstring = input[0]
pairinput = input[2:]

loops = 40
pairdict = {}

for line in pairinput:
  split = line.split(" ")
  pair = split[0]
  insert = split[2]
  pairdict[pair] = insert

# print(pairdict)

for loop in range(0, loops):
  newstring = ""
  for a in range(len(currentstring)-1):
    char1 = currentstring[a]
    char2 = currentstring[a+1]
    insert = pairdict[char1+char2]
    newstring += char1 + insert
    if a == len(currentstring)-2:
      newstring += char2
  currentstring = newstring
  print(loop)

print(currentstring)

count = Counter(currentstring)

print(count)

countnums = [count[i] for i in count]

mostcommon = max(countnums)
leastcommon = min(countnums)

print(mostcommon-leastcommon)
